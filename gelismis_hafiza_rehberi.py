import os 
from agents import Agent, Runner, SQLiteSession

os.environ["OPENAI_API_KEY"] = ""

def main():
    print("=== ÖRNEK 1: Bellek İçi Oturum (':memory:') ===")

    memory_agent = Agent(name="TestAsistan", instructions="Kısa ve net cevaplar ver.")
    gecici_session = SQLiteSession(session_id="test_kullanici", db_path=":memory:")

    res1 = Runner.run_sync(memory_agent, "Gizli sayı 42'dir." ,session=gecici_session)
    print("1. Tur Yanıtı:, res1.final_output")

    res2 = Runner.run_sync(memory_agent, "Gizli sayı kaçtı?", session=gecici_session)
    print("2. Tur (RAM Hafızası) Ynaıtı:", res2.final_output)
    print("*(Not: Bu script kapanınca bu veriler RAM'den silinecektir.)*")



    print("=== ÖRNEK 2: Uzuzn Süreli Hafıza & Profil Entegrasyonu ===")

    kullanici_profili = {
        "ad": "Rümeysa",
        "bolum": "Yapay Zeka Operatörlüğü",
        "favori_dil": "Python"
    }

    profil_agent = Agent(
        name="ProfilAsistanı",
        instructions=f"Kullanıcının kalıcı profili şudur: {kullanici_profili}. Bu bilgileri her zaman baz al."
    )

    res_profil = Runner.run_sync(profil_agent, "Hnagi bölümde okuyorum ve favori dilim ne?")
    print("Uzun süreli Profil Yanıtı:", res_profil.final_output)

  
  
    print("=== ÖRNEK 3: Context Window Sınırı & Özetleme Stratejisi ===")
    uzun_sohbet_ozeti = "Özet: Rümeysa Yapay Zeka okuyor, SQLiteSession ve Python üzerinde çalıştı."

    temiz_session = SQLiteSession(session_id="rumeysa_temiz_oturum", db_path="sohbet.db")

    res_devam = Runner.run_sync(
        profil_agent,
        f"Önceki konuşmalarımızın özeti: {uzun_sohbet_ozeti}. Buradan devam edelim, ben ne okuyordum?",
        session=temiz_session
    )
    print("Özetlenmiş Yeni Oturum Yanıtı:", res_devam.final_output)

if __name__ == "__main__":
    main()    