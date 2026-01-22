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
# HELPERS
# -----------------------------
def get_rulership_list(planet_row, mode: str):
    if mode == "Klasik":
        r = planet_row["rulership_classic"]
    elif mode == "Modern":
        r = planet_row["rulership_modern"]
    else:
        r = sorted(list(set(planet_row["rulership_classic"] + planet_row["rulership_modern"])))
    return r

def build_rule_based_commentary(planet: str, themes: str, house_title: str, house_keywords: str, active_ruler: str | None):
    ruler_txt = f"Aktif yönetici burç: **{active_ruler}**." if active_ruler else "Aktif yönetici burç seçilmedi."
    out = []
    out.append(f"### {planet} {house_title} — Kural tabanlı yorum")
    out.append(ruler_txt)
    out.append("")
    out.append("**Güçlü yönler**")
    out.append(f"- {house_title} ({house_keywords}) alanında {planet.lower()} temaları ({themes}) güçlü çalışır.")
    out.append("- İletişim/karar/odak (gezegene göre) daha görünür ve belirleyici olur.")
    out.append("")
    out.append("**Gölge taraflar**")
    out.append("- Konuları fazla zihinselleştirme / aşırı kontrol / abartma (gezegenin doğasına göre) görülebilir.")
    out.append("- İlişki/ortaklık gibi alanlarda “haklılık” ile “uyum” arasında gerilim oluşabilir.")
    out.append("")
    out.append("**Hayata yansıması (örnek alanlar)**")
    out.append("- İlişkilerde: konuşarak çözme isteği artar; fakat dilin keskinleşmesi tartışma doğurabilir.")
    out.append("- İşte: ortaklı işler, danışmanlık, müşteri yönetimi, sözleşmeler öne çıkabilir.")
    out.append("")
    out.append("**Uygulanabilir 3 öneri**")
    out.append("- Önemli konuşmaları yazılı netleştir (madde madde).")
    out.append("- Haftalık “check-in” rutini kur: beklenti, sınır, ihtiyaç.")
    out.append("- Karar anında 24 saat kuralı: tepki yerine yanıt üret.")
    return "\n".join(out)

# -----------------------------
# UI
# -----------------------------
st.title("Astro Tablo: Evler + Gezegen Temaları + Yönettiği Burçlar")

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    house_no = st.selectbox("Ev seç", df_houses["house"].tolist(), index=6)  # 7. ev default
with col2:
    planet_name = st.selectbox("Gezegen seç", df_planets["planet"].tolist(), index=2)  # Merkür default
with col3:
    mode = st.radio("Yöneticilik modu", ["Klasik", "Modern", "Klasik + Modern"], horizontal=True)

house_row = df_houses[df_houses["house"] == house_no].iloc[0]
planet_row = df_planets[df_planets["planet"] == planet_name].iloc[0]

rulership = get_rulership_list(planet_row, mode)

# Eğer 2+ burç yönetiyorsa: tekini seçtir
active_ruler = None
if len(rulership) == 1:
    active_ruler = rulership[0]
elif len(rulership) > 1:
    active_ruler = st.selectbox("Aktif yönetici burcu seç (tek burçla ilerle)", rulership, index=0)

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
        st.caption(f"Aktif yönetici burç: {active_ruler}" if active_ruler else "Aktif yönetici burç seçiniz.")
    else:
        st.info("Bu gezegen için seçilen modda yöneticilik listesi boş.")

with right:
    st.subheader("🧠 Yorumlama")
    st.caption("Butona basınca kural tabanlı yorum üretir (LLM çağırmaz).")

    if st.button("Yorumu üret", type="primary"):
        commentary = build_rule_based_commentary(
            planet=planet_row["planet"],
            themes=planet_row["themes"],
            house_title=house_row["title"],
            house_keywords=house_row["keywords"],
            active_ruler=active_ruler
        )
        st.session_state["commentary"] = commentary

    commentary_text = st.session_state.get("commentary", "")
    if commentary_text:
        st.markdown(commentary_text)
    else:
        st.info("Yorum henüz üretilmedi. 'Yorumu üret' butonuna bas.")

    st.subheader("🗣️ LLM için prompt çıktısı")
    prompt = f"""
Aşağıdaki astrolojik kombinasyonu yorumla ve 6-10 maddelik pratik içgörü üret:

- Gezegen: {planet_row['planet']}
- Gezegen temaları: {planet_row['themes']}
- Gezegenin yönettiği burçlar ({mode}): {', '.join(rulership) if rulership else '—'}
- Aktif yönetici burç (tek burç): {active_ruler if active_ruler else '—'}
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
