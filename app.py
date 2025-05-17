import streamlit as st
from query_parser import parse_query
from retriever import retrieve_products
from gemini_gen import generate_description

st.title("💻 GenAI Laptop Finder")

query = st.text_input("Ask your query (e.g., Budget laptop for remote work):")

if st.button("Search") and query:
    with st.spinner("Understanding your query..."):
        parsed = parse_query(query)
        laptops = retrieve_products(parsed)

        if laptops:
            st.subheader("Top Laptop Picks:")
            for laptop in laptops:
                st.markdown(f"### {laptop['name']} (${laptop['price']})")
                st.markdown(f"- **Battery:** {laptop['battery_life']}")
                st.markdown(f"- **Brand:** {laptop['brand']}")
                st.markdown(f"- **Specs:** {laptop['specs']}")

                with st.spinner("Generating AI description..."):
                    desc = generate_description(laptop)
                    st.success(desc)
                st.markdown("---")
        else:
            st.warning("No matching laptops found.")