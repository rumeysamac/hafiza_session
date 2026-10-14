import os
from agents import Agent, Runner, SQLiteSession


os.environ["OPENAI_API_KEY"] = ""


agent = Agent(
    name="RehberAsistan",
    instructions="Kısa, net ve yardımsever cevaplar ver."
)

print("--- 1. KISIM: Kısa Süreli Hafıza (Manuel to_input_list) ---")

gecmis_listesi = []

gecmis_listesi.append({"role": "user", "content": "Gizli kelimem: 'YapayZeka2026'."})
sonuc1 = Runner.run_sync(agent, gecmis_listesi)
gecmis_listesi = sonuc1.to_input_list() # Geçmişi listeye güncelliyoruz

gecmis_listesi.append({"role": "user", "content": "Gizli kelimem neydi?"})
sonuc2 = Runner.run_sync(agent, gecmis_listesi)
print("Manuel Asistan Yanıtı:", sonuc2.final_output)


print("\n--- 2. KISIM: Uzun Süreli ve Çoklu Kullanıcı Yönetimi (SQLiteSession) ---")
# Aynı veritabanı içinde iki farklı kullanıcı için ayrı oturumlar (session_id) açıyoruz
session_rumeysa = SQLiteSession(session_id="kullanici_rumeysa", db_path="egitim_hafiza.db")
session_tuğba = SQLiteSession(session_id="kullanici_ahmet", db_path="egitim_hafiza.db")

# Rümeysa kendine özel oturumda kendini tanıtıyor
Runner.run_sync(
    agent, 
    "Benim adım Rümeysa ve yapay zeka okuyorum.", 
    session=session_rumeysa
)

# Tuğba kendine özel oturumda kendini tanıtıyor
Runner.run_sync(
    agent, 
    "Merhaba, ben Tuğba ve bilgisayar programcılığı okuyorum.", 
    session=session_tuğba
)


rumeysa_kontrol = Runner.run_sync(
    agent, 
    "Benim adim ne ve ne okuyorum?", 
    session=session_rumeysa
)
print("Rümeysa'nın Oturumu Sonucu:", rumeysa_kontrol.final_output)


tuğba_kontrol = Runner.run_sync(
    agent, 
    "Benim adim ne ve ne okuyorum?", 
    session=session_tuğba
)
print("Tuğba'nın Oturumu Sonucu:", tuğba_kontrol.final_output)