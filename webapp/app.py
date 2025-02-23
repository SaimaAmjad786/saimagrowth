
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="⭐")

# Initialize session state
if "quotes" not in st.session_state:
    st.session_state.quotes = []
if "comments" not in st.session_state:
    st.session_state.comments = []
if "subscribed" not in st.session_state:
    st.session_state.subscribed = False

# Title
st.title("Growth Mindset Challenge: Web App With Streamlit 🔎")

# Welcome Section
st.header("🚀 Welcome to Your Growth Journey!")
st.write(
    "Embrace challenges, learn from mistakes, and unlock your full potential. "
    "This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! ⭐"
)

# Quote Section
st.header("💡 Today's Growth Mindset")
st.write("**Success is not final, failure is not fatal: it is the courage to continue that counts.** - Winston Churchill")

# Challenge Input
st.header("✍ What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")
if user_input.strip():
    st.success(f"💪 You are facing: {user_input.strip()}. Keep pushing forward toward your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Quote Saving Section
st.header(" ✏️ Save Your Favorite Quote")
quote_input = st.text_input("Enter a motivational quote:")
if st.button("💡 Save Quote"):
    if quote_input.strip():
        st.session_state.quotes.append(quote_input.strip())
        st.success("✨ Quote Saved!")
    else:
        st.warning("Please enter a quote before saving.")

# Display Saved Quotes
st.header(" 📖 Your Saved Quotes")
if st.session_state.quotes:
    for quote in st.session_state.quotes:
        st.write(f"- {quote}")
else:
    st.info("No quotes saved yet. Start adding your favorite quotes!")

# Reflection Section
st.header("📝 Reflection on Your Learning")
st.write("Every experience teaches us something valuable. Share a lesson you learned recently:")
reflection = st.text_area("Write your reflections here:")
if reflection.strip():
    st.success(f"🌞 Great insight! Your reflection: {reflection.strip()}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

# Achievement Section
st.header("🙋 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")
if achievement.strip():
    st.success(f"✨ Amazing! You achieved: {achievement.strip()}")
else:
    st.info("😊 Big or small, every achievement counts! Share one now. 😍")

# More Motivation Button
if st.button("💡 More Motivation"):
    st.balloons()
    st.success("✨ You are doing great! Every step you take is a step toward growth. Keep going! 🚀")

# Interaction Section
st.markdown("## Show some love! ❤️")
col1, col2 = st.columns(2)

with col1:
    if st.button("👍 Like"):
        st.write("Thank you for liking ❤️")
        st.snow()

# Comment Section with Save and Delete Options
st.header("💬 Community Comments")

comment_input = st.text_area("Leave a comment:")
if st.button("Submit Comment"):
    if comment_input.strip():
        st.session_state.comments.append(comment_input.strip())
        st.success("✅ Your comment has been recorded!")
        st.rerun()
    else:
        st.warning("Please enter a comment before submitting.")

# Display and manage saved comments
if st.session_state.comments:
    st.subheader("📌 Saved Comments:")
    for index, comment in enumerate(st.session_state.comments):
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.write(f"- {comment}")
        with col2:
            if st.button("❌", key=f"delete_{index}"):
                del st.session_state.comments[index]
                st.rerun()
else:
    st.info("No comments yet. Be the first to share your thoughts!")

# Subscribe Section
st.header("🔔 Subscribe for More Motivation!")

if not st.session_state.subscribed:
    if st.button("Subscribe"):
        st.session_state.subscribed = True
        st.success("🎉 Successfully Subscribed!")
        st.balloons()
else:
    st.info("✅ You are already subscribed!")

# Footer
st.write("---")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**🎯 Created by Saima Amjad**")