import streamlit as st
from word_list import word_list
from class_main import Smart_Vocab

# 세션 상태 초기화
if "trainer" not in st.session_state:
    st.session_state.trainer = Smart_Vocab(word_list)
    st.session_state.trainer.start_learn()
if "current_word" not in st.session_state:
    st.session_state.current_word = None
if "choices" not in st.session_state:
    st.session_state.choices = None
if "answered" not in st.session_state:
    st.session_state.answered = True
if "last_result" not in st.session_state:
    st.session_state.last_result = None

st.title("📚 Smart Vocab for Denmark Sik")
st.write("매일 매일 10개씩만하자 - Yoo (Update: 2025.08.18)")

if st.button("새 단어"):
    st.session_state.current_word = st.session_state.trainer.next_word()
    st.session_state.choices = st.session_state.trainer.present_question(st.session_state.current_word)
    st.session_state.answered = False
    st.session_state.last_result = None

if st.session_state.current_word:
    st.subheader(f"Q: {st.session_state.current_word['word']}")
    if 'accent' in st.session_state.current_word:
        st.caption(f"🔊 발음: {st.session_state.current_word['accent']}")
        
        choice = st.radio("뜻을 고르세요.", st.session_state.choices, index=None, key=f"answer_{st.session_state.trainer.current_index}")

    if not st.session_state.answered and choice is not None:
        selected_index = st.session_state.choices.index(choice) + 1
        correct = st.session_state.trainer.check_answer(selected_index, st.session_state.choices)
        if correct:
            st.success(f"정답! 🎉 현재 점수: {st.session_state.trainer.score}/{st.session_state.trainer.total_words}")
            st.info(f"'{st.session_state.current_word['word']}'의 뜻은 '{st.session_state.current_word['correct_meaning']}'입니다.")
            st.session_state.answered = True
        else:
            st.error(f"틀렸습니다. 다시 선택하세요.")

st.info(f"현재 점수: {st.session_state.trainer.score}/{st.session_state.trainer.total_words}")

if st.button("학습 종료하기"):
    st.write("학습을 종료합니다.")
    st.session_state.trainer = Smart_Vocab(word_list)
    st.session_state.trainer.start_learn()
    st.session_state.current_word = None
    st.session_state.choices = None
    st.session_state.answered = True
    st.session_state.last_result = None

if st.session_state.current_word is None:
    st.write("[새 단어] 버튼을 눌러 학습을 시작하세요.")