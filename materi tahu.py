import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Ensiklopedia Tahu", page_icon="🍲", layout="centered")

# --- CSS Custom agar lebih rapi ---
st.markdown("""
    <style>
    .main {
        background-color: #fcf8f0;
    }
    h1 {
        color: #d35400;
    }
    .stExpander {
        background-color: #ffffff;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .home-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #d35400;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Menu ---
st.sidebar.title("🍱 Menu Navigasi")
menu = st.sidebar.radio("Pilih Topik:", [
    "🏠 Beranda",
    "Sejarah Tahu", 
    "Kandungan & Manfaat", 
    "Cara Pembuatan", 
    "Resep Sederhana",
    "Cara Menyimpan Tahu"
])

# --- KONTEN BERANDA (HOMEPAGE) ---
if menu == "🏠 Beranda":
    st.title("🍲 Selamat Datang di Dunia Tahu")
    st.write("Temukan segala hal tentang tahu, dari sejarah, nutrisi, hingga resep lezat di sini.")
    
    st.divider()
    
    # Bagian Informasi Usaha
    st.markdown('<div class="home-card">', unsafe_allow_html=True)
    st.subheader("🏭 Profil Produksi Utama")
    st.markdown("### **TAHU BANDUNG SPESIAL IDOLA**")
    st.write("Menyediakan tahu kualitas terbaik, segar, dan diproses secara higienis setiap hari.")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("**📍 Alamat:**")
    with col2:
        st.write("""Jl. Babakan ujung RT.03/RW.03, Kec. Sukaraja, 
        Cilebut Barat, Kab. Bogor, Provinsi Jawa Barat.""")
    
    col3, col4 = st.columns([1, 2])
    with col3:
        st.write("**📞 Kontak:**")
    with col4:
        st.write("088213924226 (Pak Bayu)")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("") # Spasi
    
    # Tombol Interaksi Cepat
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("💬 Hubungi via WhatsApp", "https://wa.me/6288213924226?text=Halo%20Tahu%20Bandung%20Idola")
    with c2:
        # Link Maps (Pencarian Alamat)
        st.link_button("🗺️ Lihat di Google Maps", "https://www.google.com/maps/search/Jl.+Babakan+ujung+RT.03%2FRW.03,+Cilebut+Barat")

    st.image("https://www.magnific.com/premium-photo/close-up-raw-tahu-kuning-yellow-tofu-bamboo-basket_34969718.htm", caption="Tahu Segar Siap Olah")

# --- KONTEN SEJARAH ---
elif menu == "Sejarah Tahu":
    st.header("⏳ Sejarah Tahu")
    st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800", caption="Tahu dalam berbagai sajian.")
    st.markdown("""
    Tahu berasal dari **Tiongkok**, tepatnya pada masa Dinasti Han sekitar 2.000 tahun yang lalu. 
    Menurut legenda, tahu ditemukan oleh **Pangeran Liu An**.
    
    Tahu kemudian menyebar ke seluruh Asia, termasuk Jepang (disebut *Tofu*) dan Indonesia, 
    di mana tahu telah menjadi bagian tak terpisahkan dari budaya kuliner masyarakat lokal.
    """)

# --- KONTEN KANDUNGAN & MANFAAT ---
elif menu == "Kandungan & Manfaat":
    st.header("💪 Kandungan & Manfaat")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Nutrisi (per 100g)")
        st.write("- Protein: 8-10g")
        st.write("- Lemak: 4-5g")
        st.write("- Kalori: 76 kkal")
        st.write("- Kalsium & Zat Besi")
    with col2:
        st.subheader("Manfaat Kesehatan")
        st.success("Menurunkan kolesterol jahat (LDL).")
        st.success("Mencegah pengeroposan tulang.")
        st.success("Membantu fungsi otak dan elastisitas kulit.")

# --- KONTEN CARA PEMBUATAN ---
elif menu == "Cara Pembuatan":
    st.header("⚙️ Proses Pembuatan")
    st.info("Berikut adalah langkah-langkah tradisional mengubah kedelai menjadi tahu:")
    steps = [
        "**Perendaman:** Kedelai direndam hingga mengembang.",
        "**Penggilingan:** Kedelai digiling dengan air menjadi susu kedelai kasar.",
        "**Perebusan:** Susu kedelai direbus hingga mendidih.",
        "**Penyaringan:** Memisahkan sari kedelai dari ampasnya (okara).",
        "**Penggumpalan:** Sari kedelai dicampur koagulan (asam/cuka) hingga menggumpal.",
        "**Pencetakan:** Gumpalan tahu dipres untuk mengeluarkan air hingga padat."
    ]
    for i, step in enumerate(steps, 1):
        st.write(f"{i}. {step}")

# --- KONTEN RESEP ---
elif menu == "Resep Sederhana":
    st.header("🍳 Resep Masakan Tahu")
    st.write("Klik pada judul resep untuk melihat bahan, langkah, dan video tutorialnya.")

    # Resep 1
    with st.expander("🌶️ Tahu Cabai Garam"):
        st.write("**Deskripsi:** Menu favorit Chinese food yang krispi dan gurih.")
        st.markdown("**Bahan:** Tahu putih, 3 sdm maizena, 5 siung baput, 10 cabai rawit, daun bawang.")
        st.markdown("**Langkah:** Balur tahu dengan maizena, goreng garing. Tumis bumbu, masukkan tahu, aduk rata.")
        st.link_button("📺 Tonton Tutorial", "https://youtu.be/y6eRAgaqi7I?si=V-EUpYVfR-Rf8rxq")

    # Resep 2
    with st.expander("🍯 Semur Tahu Kentang"):
        st.write("**Deskripsi:** Rasa manis gurih yang cocok untuk anak-anak.")
        st.markdown("**Bahan:** 5 tahu, 2 kentang (goreng), 5 sdm kecap manis, salam, serai, bumbu halus semur.")
        st.markdown("**Langkah:** Tumis bumbu, masukkan tahu-kentang, tambahkan kecap & air, masak hingga meresap.")
        st.link_button("📺 Tonton Tutorial", "https://youtu.be/borc_QEvzLw?si=WPVKwgn8qJNOug-x")

    # Resep 3
    with st.expander("🥜 Tahu Telur Khas Jawa Timur"):
        st.write("**Deskripsi:** Hidangan protein tinggi dengan saus kacang segar.")
        st.markdown("**Bahan:** 2 tahu putih, 2 telur, tauge, saus kacang (kacang tanah, baput, cabai, kecap, petis).")
        st.markdown("**Langkah:** Goreng tahu dalam telur dadar, tata dengan tauge, siram saus kacang.")
        st.link_button("📺 Tonton Tutorial", "https://youtu.be/3sxYn_zKivw?si=cu3jQEeTDC4oBD8W")

    # Resep 4
    with st.expander("🍃 Pepes Tahu Kemangi"):
        st.write("**Deskripsi:** Opsi sehat tanpa minyak goreng.")
        st.markdown("**Bahan:** 5 tahu (hancurkan), kemangi, 1 telur, bumbu halus pepes.")
        st.markdown("**Langkah:** Campur adonan, bungkus daun pisang, kukus 25 menit.")
        st.link_button("📺 Tonton Tutorial", "https://youtu.be/5sXx5xVf_p0?si=0OoFracT4y54dv7L")

    # Resep 5
    with st.expander("🏮 Tahu Mapo (Mapo Tofu)"):
        st.write("**Deskripsi:** Hidangan lembut, pedas, dan bergaya oriental.")
        st.markdown("**Bahan:** 2 tahu sutra, 100g daging cincang, saus sambal, saus tiram, minyak wijen, maizena.")
        st.markdown("**Langkah:** Tumis daging & bumbu, masukkan tahu sutra, kentalkan dengan maizena.")
        st.link_button("📺 Tonton Tutorial", "https://youtu.be/_NICwQILeTo?si=hDlnmpH_Q3R-DamX")

# --- KONTEN PENYIMPANAN ---
elif menu == "Cara Menyimpan Tahu":
    st.header("🧊 Tips Penyimpanan Tahu")
    st.warning("Tahu mudah basi karena kadar airnya tinggi. Gunakan cara ini agar awet hingga 1 minggu.")
    st.subheader("1. Cuci & Bersihkan")
    st.write("Cuci tahu dengan air mengalir untuk menghilangkan lendir.")
    st.subheader("2. Rendam Air Matang")
    st.info("Simpan dalam wadah tertutup. Pastikan tahu terendam air matang dingin.")
    st.subheader("3. Perawatan di Kulkas")
    st.write("Simpan di chiller dan wajib ganti airnya setiap hari.")

# --- Footer ---
st.divider()
st.caption("Dibuat dengan Python & Streamlit | Tahu Bandung Spesial Idola © 2026")
