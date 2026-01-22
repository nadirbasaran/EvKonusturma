import streamlit as st
import pandas as pd

st.set_page_config(page_title="Astro Ev + Gezegen Tablosu", layout="wide")

# -----------------------------
# DATA
# -----------------------------
HOUSES = [
    {"house": 1, "title": "1. Ev", "keywords": "Benlik, beden, dış imaj, başlangıçlar"},
    {"house": 2, "title": "2. Ev", "keywords": "Para, özdeğer, sahip oldukların, güvenlik"},
    {"house": 3, "title": "3. Ev", "keywords": "İletişim, öğrenme, kardeşler, kısa yolculuklar"},
    {"house": 4, "title": "4. Ev", "keywords": "Ev-aile, kökler, iç güvenlik, özel hayat"},
    {"house": 5, "title": "5. Ev", "keywords": "Aşk, keyif, yaratıcılık, çocuklar, hobiler"},
    {"house": 6, "title": "6. Ev", "keywords": "Günlük düzen, iş rutini, sağlık, hizmet"},
    {"house": 7, "title": "7. Ev", "keywords": "İlişkiler, evlilik, ortaklık, açık düşmanlar"},
    {"house": 8, "title": "8. Ev", "keywords": "Dönüşüm, kriz, ortak para, miras, mahremiyet"},
    {"house": 9, "title": "9. Ev", "keywords": "İnanç, yüksek eğitim, uzak yolculuklar, vizyon"},
    {"house": 10, "title": "10. Ev", "keywords": "Kariyer, statü, hedefler, otorite"},
    {"house": 11, "title": "11. Ev", "keywords": "Arkadaşlar, çevre, topluluklar, gelecek planları"},
    {"house": 12, "title": "12. Ev", "keywords": "Bilinçdışı, kapanışlar, izolasyon, ruhsallık"},
]

PLANETS = [
    {"planet": "Güneş", "themes": "Kimlik, irade, yaşam enerjisi, görünürlük", "rulership_classic": ["Aslan"], "rulership_modern": ["Aslan"]},
    {"planet": "Ay", "themes": "Duygu, güvenlik, alışkanlıklar, bakım", "rulership_classic": ["Yengeç"], "rulership_modern": ["Yengeç"]},
    {"planet": "Merkür", "themes": "Zihin, iletişim, öğrenme, analiz", "rulership_classic": ["İkizler", "Başak"], "rulership_modern": ["İkizler", "Başak"]},
    {"planet": "Venüs", "themes": "İlişki, değerler, estetik, uyum", "rulership_classic": ["Boğa", "Terazi"], "rulership_modern": ["Boğa", "Terazi"]},
    {"planet": "Mars", "themes": "Eylem, cesaret, arzu, rekabet", "rulership_classic": ["Koç", "Akrep"], "rulership_modern": ["Koç"]},
    {"planet": "Jüpiter", "themes": "Büyüme, şans, anlam, inanç", "rulership_classic": ["Yay", "Balık"], "rulership_modern": ["Yay"]},
    {"planet": "Satürn", "themes": "Sınır, sorumluluk, yapı, zaman", "rulership_classic": ["Oğlak", "Kova"], "rulership_modern": ["Oğlak"]},
    {"planet": "Uranüs", "themes": "Özgürleşme, yenilik, sürpriz, kopuş", "rulership_classic": [], "rulership_modern": ["Kova"]},
    {"planet": "Neptün", "themes": "Sezgi, hayal, çözülme, idealizm", "rulership_classic": [], "rulership_modern": ["Balık"]},
    {"planet": "Plüton", "themes": "Güç, dönüşüm, kriz/yeniden doğuş, derinlik", "rulership_classic": [], "rulership_modern": ["Akrep"]},
]

df_houses = pd.DataFrame(HOUSES)
df_planets = pd.DataFrame(PLANETS)

# -----------------------------
# UI
# -----------------------------
st.title("Astro Tablo: Evler + Gezegen Temaları + Yönettiği Burçlar")

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    house_no = st.selectbox("Ev seç", df_houses["house"].tolist(), index=6)  # default 7. ev
with col2:
    planet_name = st.selectbox("Gezegen seç", df_planets["planet"].tolist(), index=0)  # default Güneş
with col3:
    mode = st.radio("Yöneticilik modu", ["Klasik", "Modern", "Klasik + Modern"], horizontal=True)

house_row = df_houses[df_houses["house"] == house_no].iloc[0]
planet_row = df_planets[df_planets["planet"] == planet_name].iloc[0]

if mode == "Klasik":
    rulership = planet_row["rulership_classic"]
elif mode == "Modern":
    rulership = planet_row["rulership_modern"]
else:
    rulership = sorted(list(set(planet_row["rulership_classic"] + planet_row["rulership_modern"])))

# -----------------------------
# OUTPUT
# -----------------------------
left, right = st.columns(2)

with left:
    st.subheader("📌 Seçilen Ev")
    st.write(f"**{house_row['title']}**")
    st.write(house_row["keywords"])

    st.subheader("🪐 Seçilen Gezegen")
    st.write(f"**{planet_row['planet']}**")
    st.write(planet_row["themes"])

    st.subheader("♟️ Yönettiği Burçlar")
    if rulership:
        st.write(", ".join(rulership))
    else:
        st.info("Bu gezegen için seçilen modda yöneticilik listesi boş.")

with right:
    st.subheader("🧠 Kural tabanlı mini yorum (taslak)")
    mini = (
        f"{planet_row['planet']} {house_row['title']} konularında "
        f"({house_row['keywords']}) daha görünür çalışır. "
        f"Teması: {planet_row['themes']}. "
        f"Yönettiği burçlar: {', '.join(rulership) if rulership else '—'}."
    )
    st.write(mini)

    st.subheader("🗣️ LLM için prompt çıktısı")
    prompt = f"""
Aşağıdaki astrolojik kombinasyonu yorumla ve 6-10 maddelik pratik içgörü üret:

- Gezegen: {planet_row['planet']}
- Gezegen temaları: {planet_row['themes']}
- Gezegenin yönettiği burçlar ({mode}): {', '.join(rulership) if rulership else '—'}
- Ev: {house_row['title']}
- Ev anahtar kelimeleri: {house_row['keywords']}

Yorumda:
1) güçlü yönler,
2) gölge taraflar,
3) ilişki/iş/para gibi alanlara olası yansımalar,
4) uygulanabilir 3 öneri
olsun.
""".strip()

    st.code(prompt, language="text")
    st.download_button("Prompt'u TXT indir", data=prompt, file_name="astro_prompt.txt")

st.divider()

st.subheader("📊 Ham tablolar")
tab1, tab2 = st.tabs(["Evler", "Gezegenler"])
with tab1:
    st.dataframe(df_houses, use_container_width=True)
with tab2:
    st.dataframe(df_planets, use_container_width=True)

