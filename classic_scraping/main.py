import streamlit as st
from scrape_classic import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Option to save interactions
save_interactions = st.checkbox("Save interactions with LLM", value=False)

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Scrape the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = cleaned_content
        st.session_state.scraped = True  # Flag to indicate scraping is complete

# Display the DOM content only if it's available
if st.session_state.get("scraped"):
    # Display the DOM content in an expandable text box
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", st.session_state.dom_content, height=300)

    # Step 2: Ask Questions About the DOM Content
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description, save_interactions)

            # Store parsed result in session state to allow for later use if needed
            st.session_state.parse_result = parsed_result

            # Save interaction if checkbox is selected and action was performed
            if save_interactions:
                st.write("Interaction saved.")

            # Display the parsed result
            st.write("LLM Answer:")
            st.write(parsed_result)
