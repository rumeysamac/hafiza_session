import os
from agents import Agent, Runner, SQLiteSession


os.environ["OPENAI_API_KEY"] = ""

agent = Agent(
    name="Asistan",
    instructions="Kısa ve net cevaplar ver. Kullanıcının sunduğu bilgileri unutma."
)

session_rumeysa = SQLiteSession(session_id="kullanici_rumeysa", db_path="sohbet.db")

def main():
    print("--- 1. Tur: Kullanıcı Kendini Tanıtıyor ---")
    res1 = Runner.run_sync(
        agent, 
        "Benim adım Rümeysa ve yapay zeka okuyorum.", 
        session=session_rumeysa
    )
    print("Asistan Cevabı:", res1.final_output)

    print("\n--- 2. Tur: Hafıza Sorgulanıyor ---")
    res2 = Runner.run_sync(
        agent, 
        "Benim adım neydi ve ne okuyordum?", 
        session=session_rumeysa
    )
    print("Asistan Cevabı:", res2.final_output)

if __name__ == "__main__":
    main()