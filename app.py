import streamlit as st
from datetime import datetime

st.set_page_config(page_title="STYLED — Premium Clothing", page_icon="✦", layout="wide")

PRODUCTS = [
    {"id": 1, "name": "Essential Crew Neck Tee", "category": "T-Shirts", "price": 34, "original_price": 44,
     "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400",
     "desc": "Premium heavyweight cotton tee with a relaxed fit. Garment-dyed for a lived-in feel.",
     "sizes": ["XS","S","M","L","XL"], "rating": 4.5, "reviews": 128, "badge": "Sale"},
    {"id": 2, "name": "Oversized Hoodie", "category": "Hoodies", "price": 78,
     "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400",
     "desc": "Ultra-soft brushed fleece with oversized silhouette and dropped shoulders.",
     "sizes": ["S","M","L","XL","XXL"], "rating": 4.8, "reviews": 256, "badge": "New"},
    {"id": 3, "name": "Bomber Jacket", "category": "Jackets", "price": 145,
     "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400",
     "desc": "Classic bomber in premium nylon satin with ribbed collar and cuffs.",
     "sizes": ["S","M","L","XL"], "rating": 4.6, "reviews": 89, "badge": "New"},
    {"id": 4, "name": "Relaxed Fit Chino", "category": "Pants", "price": 68, "original_price": 85,
     "image": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=400",
     "desc": "Midweight stretch cotton chinos with a relaxed straight leg.",
     "sizes": ["S","M","L","XL"], "rating": 4.3, "reviews": 167, "badge": "Sale"},
    {"id": 5, "name": "Cargo Shorts", "category": "Shorts", "price": 52,
     "image": "https://images.unsplash.com/photo-1565084888279-aca607ecce0c?w=400",
     "desc": "Durable cotton cargo shorts with utility pockets.",
     "sizes": ["XS","S","M","L","XL"], "rating": 4.2, "reviews": 94, "badge": ""},
    {"id": 6, "name": "Striped Oxford Shirt", "category": "T-Shirts", "price": 58,
     "image": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400",
     "desc": "Classic oxford weave with button-down collar and chest pocket.",
     "sizes": ["S","M","L","XL"], "rating": 4.4, "reviews": 73, "badge": ""},
    {"id": 7, "name": "Vintage Wash Hoodie", "category": "Hoodies", "price": 72, "original_price": 90,
     "image": "https://images.unsplash.com/photo-1578768079052-aa76e52ff62e?w=400",
     "desc": "Garment-dyed fleece with worn-in vintage look and kangaroo pocket.",
     "sizes": ["S","M","L","XL","XXL"], "rating": 4.7, "reviews": 203, "badge": "Sale"},
    {"id": 8, "name": "Leather Craft Belt", "category": "Accessories", "price": 45,
     "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400",
     "desc": "Full-grain leather belt with brushed brass buckle.",
     "sizes": ["S","M","L","XL"], "rating": 4.1, "reviews": 45, "badge": "New"},
    {"id": 9, "name": "Wool Blend Beanie", "category": "Accessories", "price": 28,
     "image": "https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?w=400",
     "desc": "Ribbed knit beanie in wool-acrylic blend, fleece-lined.",
     "sizes": ["S","M","L"], "rating": 4.0, "reviews": 38, "badge": ""},
    {"id": 10, "name": "Denim Jacket", "category": "Jackets", "price": 120, "original_price": 150,
     "image": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=400",
     "desc": "Classic denim jacket in heavyweight rigid denim.",
     "sizes": ["S","M","L","XL"], "rating": 4.5, "reviews": 112, "badge": "Sale"},
    {"id": 11, "name": "Linen Blend Trousers", "category": "Pants", "price": 75,
     "image": "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=400",
     "desc": "Lightweight linen-cotton blend trousers with easy elastic waist.",
     "sizes": ["S","M","L","XL"], "rating": 4.3, "reviews": 56, "badge": "New"},
    {"id": 12, "name": "Graphic Logo Tee", "category": "T-Shirts", "price": 38,
     "image": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=400",
     "desc": "Bold graphic print tee in heavyweight ringspun cotton, oversized fit.",
     "sizes": ["XS","S","M","L","XL","XXL"], "rating": 4.6, "reviews": 189, "badge": ""},
]

CATEGORIES = ["All", "T-Shirts", "Hoodies", "Jackets", "Pants", "Shorts", "Accessories"]

CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: #ffffff; }
    section[data-testid="stSidebar"] { display: none; }

    .brand { font-size: 1.8rem; font-weight: 800; letter-spacing: -0.02em; }
    .brand span { color: #999; }

    .hero { padding: 80px 0 60px; }
    .hero h1 { font-size: 4rem; font-weight: 800; line-height: 1.1; letter-spacing: -0.03em; margin-bottom: 16px; }
    .hero h1 span { color: #ccc; }
    .hero p { font-size: 1.1rem; color: #666; max-width: 500px; line-height: 1.7; margin-bottom: 32px; }
    .hero-tag { font-size: 0.7rem; letter-spacing: 0.2em; color: #999; text-transform: uppercase; margin-bottom: 20px; }

    .btn-primary { display: inline-block; background: #000; color: #fff; padding: 14px 36px; font-weight: 600; font-size: 0.9rem; border-radius: 0; text-decoration: none; border: 2px solid #000; transition: all 0.2s; cursor: pointer; }
    .btn-primary:hover { background: #333; border-color: #333; }
    .btn-outline { display: inline-block; background: transparent; color: #000; padding: 14px 36px; font-weight: 600; font-size: 0.9rem; border-radius: 0; text-decoration: none; border: 2px solid #000; transition: all 0.2s; cursor: pointer; margin-left: 12px; }
    .btn-outline:hover { background: #000; color: #fff; }

    .section-title { font-size: 1.8rem; font-weight: 700; margin-bottom: 8px; }
    .section-sub { color: #999; font-size: 0.9rem; margin-bottom: 32px; }

    .product-card { border-radius: 12px; overflow: hidden; transition: transform 0.2s; margin-bottom: 16px; cursor: pointer; }
    .product-card:hover { transform: translateY(-2px); }
    .product-img { width: 100%; aspect-ratio: 4/5; object-fit: cover; border-radius: 12px; }
    .product-info { padding: 12px 0; }
    .product-cat { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: #999; font-weight: 600; }
    .product-name { font-weight: 600; font-size: 0.95rem; margin: 4px 0; }
    .product-price { font-weight: 700; font-size: 1rem; }
    .product-oprice { color: #bbb; text-decoration: line-through; font-size: 0.85rem; margin-left: 6px; }
    .product-rating { font-size: 0.8rem; color: #666; margin-top: 4px; }
    .badge { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; position: absolute; top: 12px; }
    .badge-sale { background: #dc2626; color: #fff; left: 12px; }
    .badge-new { background: #000; color: #fff; right: 12px; }

    .cart-item { display: flex; align-items: center; gap: 16px; padding: 16px 0; border-bottom: 1px solid #f0f0f0; }
    .cart-img { width: 80px; height: 100px; object-fit: cover; border-radius: 8px; }
    .cart-item-name { font-weight: 600; }
    .cart-item-meta { font-size: 0.85rem; color: #666; }
    .cart-item-price { font-weight: 700; margin-left: auto; }

    .features { background: #f8f8f8; padding: 60px 0; margin-top: 60px; }
    .feature-icon { width: 48px; height: 48px; background: #000; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin: 0 auto 16px; }
    .feature-title { font-weight: 600; margin-bottom: 4px; }
    .feature-desc { color: #999; font-size: 0.9rem; }

    .footer { text-align: center; padding: 40px 0; color: #999; font-size: 0.85rem; border-top: 1px solid #f0f0f0; margin-top: 40px; }

    div[data-testid="stButton"] button { border-radius: 0; font-weight: 600; font-size: 0.85rem; }
    div.stSelectbox label, div.stNumberInput label { font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #999; }

    .stTabs [data-baseweb="tab-list"] { gap: 0; }
    .stTabs [data-baseweb="tab"] { font-weight: 600; font-size: 0.9rem; }

    .product-detail-img { width: 100%; border-radius: 12px; }
    .product-detail-title { font-size: 2rem; font-weight: 700; margin-bottom: 12px; }
    .product-detail-price { font-size: 2rem; font-weight: 800; margin-bottom: 20px; }
    .product-detail-desc { color: #666; line-height: 1.7; margin-bottom: 24px; }
    .product-detail-label { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: #999; margin-bottom: 8px; }
</style>
"""

def init_state():
    for key in ["cart", "page", "selected_product", "checkout"]:
        if key not in st.session_state:
            st.session_state[key] = [] if key == "cart" else ("" if key in ["page","selected_product"] else False)

def header():
    c = st.columns([1, 4, 1])
    with c[0]:
        st.markdown('<div class="brand">STYLED <span>✦</span></div>', unsafe_allow_html=True)
    with c[1]:
        tabs = st.tabs([" Home ", " Shop ", " Cart ", " Checkout "])
        for i, tab_name in enumerate(["", "shop", "cart", "checkout"]):
            with tabs[i]:
                st.session_state.page = tab_name
    with c[2]:
        cart_count = sum(i["qty"] for i in st.session_state.cart)
        st.markdown(f'<div style="text-align:right;font-weight:600">Cart ({cart_count})</div>', unsafe_allow_html=True)

def home_page():
    st.markdown("""
    <div class="hero">
        <div class="hero-tag">New Collection 2026</div>
        <h1>Define Your<br><span>Style</span></h1>
        <p>Premium essentials crafted for the modern wardrobe. Timeless pieces that blend comfort with attitude.</p>
    </div>
    """, unsafe_allow_html=True)
    c = st.columns([1, 1, 1])
    with c[0]:
        if st.button("SHOP NOW", use_container_width=True, type="primary"):
            st.session_state.page = "shop"
            st.rerun()
    with c[1]:
        if st.button("VIEW COLLECTION", use_container_width=True):
            st.session_state.page = "shop"
            st.rerun()

    st.markdown('<div class="section-title">Featured</div><div class="section-sub">Curated just for you</div>', unsafe_allow_html=True)
    featured = [p for p in PRODUCTS if p["badge"]][:4]
    cols = st.columns(4)
    for i, p in enumerate(featured):
        with cols[i]:
            badge_class = "badge-sale" if p["badge"] == "Sale" else "badge-new"
            badge_pos = "left" if p["badge"] == "Sale" else "right"
            st.markdown(f'<div style="position:relative"><img src="{p["image"]}" class="product-img">'
                        f'<span class="badge {badge_class}" style="{badge_pos}:12px">{p["badge"]}</span></div>'
                        f'<div class="product-info"><div class="product-cat">{p["category"]}</div>'
                        f'<div class="product-name">{p["name"]}</div>'
                         f'<div class="product-price">${p["price"]}{(" <span class=product-oprice>$" + str(p["original_price"]) + "</span>") if p.get("original_price") else ""}</div>'
                         f'<div class="product-rating">★ {p["rating"]} ({p["reviews"]})</div></div>', unsafe_allow_html=True)
            if st.button("Quick Add", key=f"ha{p['id']}", use_container_width=True):
                st.session_state.cart.append({"id": p["id"], "name": p["name"], "price": p["price"],
                    "image": p["image"], "size": p["sizes"][0], "qty": 1})
                st.rerun()

    st.markdown("""
    <div class="features">
    <div style="max-width:1000px;margin:auto"><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:40px;text-align:center">
        <div><div class="feature-icon">🚚</div><div class="feature-title">Free Shipping</div><div class="feature-desc">On orders over $100</div></div>
        <div><div class="feature-icon">🛡️</div><div class="feature-title">Secure Checkout</div><div class="feature-desc">SSL encrypted payment</div></div>
        <div><div class="feature-icon">🔄</div><div class="feature-title">Easy Returns</div><div class="feature-desc">30-day return policy</div></div>
    </div></div></div>
    """, unsafe_allow_html=True)

def shop_page():
    st.markdown('<div class="section-title" style="margin-top:20px">Shop All</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 4])
    with col1:
        cat = st.selectbox("Category", CATEGORIES, label_visibility="collapsed")
    with col2:
        sort = st.selectbox("Sort", ["Featured", "Price: Low to High", "Price: High to Low", "Rating"], label_visibility="collapsed")

    filtered = PRODUCTS if cat == "All" else [p for p in PRODUCTS if p["category"] == cat]
    if sort == "Price: Low to High": filtered.sort(key=lambda x: x["price"])
    elif sort == "Price: High to Low": filtered.sort(key=lambda x: -x["price"])
    elif sort == "Rating": filtered.sort(key=lambda x: -x["rating"])

    cols = st.columns(3)
    for i, p in enumerate(filtered):
        with cols[i % 3]:
            badge_html = ""
            if p["badge"]:
                cls = "badge-sale" if p["badge"] == "Sale" else "badge-new"
                pos = "left:12px" if p["badge"] == "Sale" else "right:12px"
                badge_html = f'<span class="badge {cls}" style="{pos}">{p["badge"]}</span>'
            st.markdown(f'<div style="position:relative"><img src="{p["image"]}" class="product-img">{badge_html}</div>'
                        f'<div class="product-info"><div class="product-cat">{p["category"]}</div>'
                        f'<div class="product-name">{p["name"]}</div>'
                         f'<div class="product-price">${p["price"]}{(" <span class=product-oprice>$" + str(p["original_price"]) + "</span>") if p.get("original_price") else ""}</div>'
                        f'<div class="product-rating">★ {p["rating"]} ({p["reviews"]})</div></div>', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button("Details", key=f"sd{p['id']}", use_container_width=True):
                    st.session_state.selected_product = p["id"]
                    st.session_state.page = "detail"
                    st.rerun()
            with c2:
                if st.button("Add to Cart", key=f"sa{p['id']}", use_container_width=True):
                    st.session_state.cart.append({"id": p["id"], "name": p["name"], "price": p["price"],
                        "image": p["image"], "size": p["sizes"][0], "qty": 1})
                    st.rerun()

def product_detail():
    p = next((x for x in PRODUCTS if x["id"] == st.session_state.selected_product), None)
    if not p:
        st.session_state.page = "shop"
        st.rerun()
        return

    c1, c2 = st.columns(2)
    with c1:
        st.image(p["image"], use_container_width=True)
    with c2:
        st.markdown(f'<div class="product-cat" style="margin-top:20px">{p["category"]}</div>'
                    f'<div class="product-detail-title">{p["name"]}</div>'
                    f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:16px">'
                    f'<span style="font-weight:700">★ {p["rating"]}</span>'
                    f'<span style="color:#999">({p["reviews"]} reviews)</span></div>'
                    f'<div class="product-detail-price">${p["price"]}'
                    + (f' <span style="color:#bbb;text-decoration:line-through;font-size:1.2rem">${p["original_price"]}</span>' if p.get("original_price") else "")
                    + f'</div><div class="product-detail-desc">{p["desc"]}</div>', unsafe_allow_html=True)
        size = st.selectbox("Size", p["sizes"], key="detail_size")
        if st.button("ADD TO CART", use_container_width=True, type="primary"):
            st.session_state.cart.append({"id": p["id"], "name": p["name"], "price": p["price"],
                "image": p["image"], "size": size, "qty": 1})
            st.success("Added to cart!")
        if st.button("← Back to Shop"):
            st.session_state.page = "shop"
            st.rerun()

def cart_page():
    st.markdown('<div class="section-title" style="margin-top:20px">Shopping Cart</div>', unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info("Your cart is empty.")
        if st.button("Continue Shopping →"):
            st.session_state.page = "shop"
            st.rerun()
        return

    for i, item in enumerate(st.session_state.cart):
        c1, c2, c3 = st.columns([1, 3, 1])
        with c1:
            st.image(item["image"], width=100)
        with c2:
            st.markdown(f'<div style="font-weight:600">{item["name"]}</div>'
                        f'<div style="color:#666;font-size:0.85rem">Size: {item["size"]}</div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div style="font-weight:700;font-size:1.1rem;text-align:right">${item["price"]}</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            new_qty = st.number_input("Qty", value=item["qty"], min_value=1, max_value=10, key=f"qty{i}")
            if new_qty != item["qty"]:
                st.session_state.cart[i]["qty"] = new_qty
                st.rerun()
        with col2:
            if st.button("Remove", key=f"rm{i}"):
                st.session_state.cart.pop(i)
                st.rerun()
        st.divider()

    total = sum(i["price"] * i["qty"] for i in st.session_state.cart)
    shipping = 0 if total >= 100 else 10
    tax = total * 0.08
    grand_total = total + shipping + tax

    st.markdown(f"""
    <div style="background:#f8f8f8;padding:24px;border-radius:12px;margin-top:20px">
        <div style="display:flex;justify-content:space-between"><span style="color:#666">Subtotal</span><span>${total:.2f}</span></div>
        <div style="display:flex;justify-content:space-between"><span style="color:#666">Shipping</span><span>{"Free" if shipping == 0 else ("$" + str(round(shipping, 2)))}</span></div>
        <div style="display:flex;justify-content:space-between"><span style="color:#666">Tax</span><span>${tax:.2f}</span></div>
        <div style="display:flex;justify-content:space-between;font-weight:700;font-size:1.2rem;border-top:1px solid #ddd;padding-top:12px;margin-top:12px">
            <span>Total</span><span>${grand_total:.2f}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("← Continue Shopping", use_container_width=True):
            st.session_state.page = "shop"
            st.rerun()
    with c2:
        if st.button("PROCEED TO CHECKOUT →", use_container_width=True, type="primary"):
            st.session_state.page = "checkout"
            st.rerun()

def checkout_page():
    st.markdown('<div class="section-title" style="margin-top:20px">Checkout</div>', unsafe_allow_html=True)
    if st.session_state.checkout:
        st.balloons()
        st.markdown("""
        <div style="text-align:center;padding:60px 0">
            <div style="font-size:4rem;margin-bottom:16px">✓</div>
            <h2 style="font-weight:700">Order Confirmed!</h2>
            <p style="color:#666">Thank you for your purchase.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Back to Home"):
            st.session_state.cart = []
            st.session_state.checkout = False
            st.session_state.page = ""
            st.rerun()
        return

    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown("### Contact")
        email = st.text_input("Email", placeholder="your@email.com", label_visibility="collapsed")

        st.markdown("### Shipping")
        col1, col2 = st.columns(2)
        with col1: first = st.text_input("First name", label_visibility="collapsed", placeholder="First name")
        with col2: last = st.text_input("Last name", label_visibility="collapsed", placeholder="Last name")
        addr = st.text_input("Address", label_visibility="collapsed", placeholder="Address")
        col1, col2 = st.columns(2)
        with col1: city = st.text_input("City", label_visibility="collapsed", placeholder="City")
        with col2: state = st.text_input("State", label_visibility="collapsed", placeholder="State")
        col1, col2 = st.columns(2)
        with col1: zipc = st.text_input("ZIP", label_visibility="collapsed", placeholder="ZIP")
        with col2: country = st.selectbox("Country", ["United States", "Canada", "UK"], label_visibility="collapsed")

        st.markdown("### Payment")
        card = st.text_input("Card number", placeholder="4242 4242 4242 4242", label_visibility="collapsed")
        col1, col2 = st.columns(2)
        with col1: exp = st.text_input("MM/YY", label_visibility="collapsed", placeholder="MM/YY")
        with col2: cvc = st.text_input("CVC", label_visibility="collapsed", placeholder="CVC")

        if st.button("PLACE ORDER", use_container_width=True, type="primary"):
            st.session_state.checkout = True
            st.rerun()

    with c2:
        total = sum(i["price"] * i["qty"] for i in st.session_state.cart)
        shipping = 0 if total >= 100 else 10
        tax = total * 0.08
        st.markdown("### Order Summary")
        for item in st.session_state.cart:
            st.markdown(f"""
            <div style="display:flex;gap:12px;margin-bottom:12px">
                <img src="{item['image']}" style="width:60px;height:70px;object-fit:cover;border-radius:6px">
                <div style="flex:1"><div style="font-weight:600;font-size:0.9rem">{item['name']}</div>
                <div style="font-size:0.8rem;color:#666">{item['size']} x{item['qty']}</div>
                <div style="font-weight:600">${item['price'] * item['qty']:.2f}</div></div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown(f"""
        <div style="border-top:1px solid #eee;padding-top:12px">
            <div style="display:flex;justify-content:space-between;font-size:0.9rem"><span>Subtotal</span><span>${total:.2f}</span></div>
            <div style="display:flex;justify-content:space-between;font-size:0.9rem"><span>Shipping</span><span>{"Free" if shipping == 0 else ("$" + str(round(shipping, 2)))}</span></div>
            <div style="display:flex;justify-content:space-between;font-size:0.9rem"><span>Tax</span><span>${tax:.2f}</span></div>
            <div style="display:flex;justify-content:space-between;font-weight:700;font-size:1.1rem;border-top:1px solid #ddd;padding-top:12px;margin-top:8px">
                <span>Total</span><span>${(total + shipping + tax):.2f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    st.markdown(CSS, unsafe_allow_html=True)
    init_state()

    brand_col, nav_col, cart_col = st.columns([1, 5, 1])
    with brand_col:
        st.markdown('<div class="brand">STYLED <span>✦</span></div>', unsafe_allow_html=True)
    with nav_col:
        pages = {"🏠": "", "🛍️": "shop", "🛒": "cart"}
        cols = st.columns(len(pages))
        for i, (label, page_key) in enumerate(pages.items()):
            with cols[i]:
                is_active = st.session_state.page == page_key
                bg = "#000" if is_active else "#fff"
                color = "#fff" if is_active else "#000"
                if st.button(label, key=f"nav_{page_key}"):
                    st.session_state.page = page_key
                    st.rerun()
    with cart_col:
        cart_count = sum(i["qty"] for i in st.session_state.cart)
        st.markdown(f'<div style="text-align:right;font-weight:600;padding-top:8px">Cart ({cart_count})</div>', unsafe_allow_html=True)

    page = st.session_state.page
    if page == "" or page == "home":
        home_page()
    elif page == "shop":
        shop_page()
    elif page == "detail":
        product_detail()
    elif page == "cart":
        cart_page()
    elif page == "checkout":
        checkout_page()

    st.markdown("""
    <div class="footer">
        <strong>STYLED</strong> — Premium Clothing<br>
        © 2026 STYLED. All rights reserved.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
