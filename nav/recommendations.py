import streamlit as st
from utils import results, questions
from inference_engine import recommend_destination

def recommendations():
    st.title("Your Personalized Vacation Recommendations")
    

    if st.session_state.step < len(questions):
        st.error(f"Please complete the chat first! You have answered {st.session_state.step} out of {len(questions)} questions.")
        if st.button("Go back to Chat", use_container_width=True):
            st.session_state.page = "chat"
            st.rerun()
        return
    

    numeric_inputs = results(st.session_state.responses)

    numeric_inputs = {
        "time": numeric_inputs.get("time"),
        "budget": numeric_inputs.get("budget"),
        "weather": numeric_inputs.get("weather"),
        "duration": numeric_inputs.get("duration"),
        "distance": numeric_inputs.get("distance"),
        "type": numeric_inputs.get("vacation_type")
    }


    with st.spinner("Analyzing your preferences with Fuzzy Logic..."):
        best, top_scores = recommend_destination(numeric_inputs)

    if not best:
        st.error("We couldn't find a perfect match. Try resetting and changing your preferences!")
        return

    
    # Destinació Principal
    st.markdown(f"""
        <div style="background-color: #D3e4ff; padding: 20px; border-radius: 15px; border-left: 10px solid #1d4ed8; margin-bottom: 25px;">
            <h2 style="margin: 0; color: #1e3a8a;">Top Pick: {best}</h2>
            <p style="color: #1e3a8a; font-size: 1.1rem;">Based on your preferences, <b>{best}</b> is the ideal destination for your next trip!</p>
        </div>
    """, unsafe_allow_html=True)

    # Llista de recomanacions detallada
    st.subheader("Analysis of Top 3 Destinations")
    
    for i, (dest, score) in enumerate(top_scores.items()):

        display_score = score * 100 
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown(f"### #{i+1} {dest}")
        
        with col2:
            st.markdown(f"**Match Confidence: {display_score:.1f}%**")
            st.progress(score)

    st.divider()
    
    # Botó per veure paràmetres tècnics (OPCIONAL)
    with st.expander("See technical fuzzy inputs"):
        st.write(numeric_inputs)