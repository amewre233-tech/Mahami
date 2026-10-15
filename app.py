import streamlit as st
import datetime
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="نظام مهامي الإداري", page_icon="⏱️", layout="centered")

st.title("⏱️ نظام مهامي - إدارة وردية 9 ساعات")
st.write("نظام توزيع وتتبع 4 مهام يومية للموظفين خلال وردية العمل.")

# مدة الوردية والمهام
TOTAL_HOURS = 9
TASKS_COUNT = 4

st.sidebar.header("⚙️ لوحة التحكم الإدارية")
role = st.sidebar.radio("اختر الواجهة:", ["واجهة الموظف", "واجهة المدير"])

# رقم الهاتف للمدير لإرسال إثباتات الواتساب (ضع رقمك هنا مع رمز الدولة)
MANAGER_PHONE = "9647XXXXXXXXX" 

if role == "واجهة الموظف":
    st.subheader("📋 قائمة المهام اليومية (وردية 9 ساعات)")
    st.info("💡 ملاحظة: يتطلب إنجاز المهام الـ 4 الالتزام الكامل بالوقت المحدد لكل مهمة لتنتهي قبل نهاية الوردية بـ 5 دقائق.")
    
    # قائمة المهام الـ 4
    tasks = [
        {"id": 1, "name": "المهمة الأولى: التجهيز والمراجعة الأولى", "time": "2س و15د"},
        {"id": 2, "name": "المهمة الثانية: تنفيذ الجزء الأكبر من العمل", "time": "2س و15د"},
        {"id": 3, "name": "المهمة الثالثة: المتابعة والتدقيق", "time": "2س و15د"},
        {"id": 4, "name": "المهمة الرابعة: إعداد التقرير النهائي والتسليم", "time": "2س و10د"}
    ]

    completed_count = 0

    for task in tasks:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{task['name']} *(الوقت المقدر: {task['time']})*")
        with col2:
            is_done = st.checkbox("Done ✅", key=f"task_{task['id']}")
            if is_done:
                completed_count += 1

    st.divider()
    
    # شريط التقدم
    progress = completed_count / TASKS_COUNT
    st.progress(progress)
    st.write(f"تم إنجاز {completed_count} من أصل {TASKS_COUNT} مهام.")

    # قسم إرسال التوثيق عبر الواتساب
    st.subheader("📸 إرسال إثبات الإنجاز عبر الواتساب")
    uploaded_file = st.file_uploader("ارفع صورة إثبات العمل:", type=["jpg", "jpeg", "png"])
    
    msg_text = f"تم إنجاز {completed_count}/{TASKS_COUNT} من مهام اليوم في نظام مهامي."
    whatsapp_url = f"https://wa.me/{MANAGER_PHONE}?text={urllib.parse.quote(msg_text)}"
    
    st.markdown(f'''
        <a href="{whatsapp_url}" target="_blank">
            <button style="background-color:#25D366; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; font-size:16px;">
                📲 إرسال الإثبات إلى المدير عبر الواتساب
            </button>
        </a>
    ''', unsafe_allow_html=True)

elif role == "واجهة المدير":
    st.subheader("📊 لوحة متابعة المدير")
    st.success("أنت الآن تتابع سير العمل والمهام المسندة للموظفين.")
    st.write("• حالة الوردية: شغالة (9 ساعات)")
    st.write("• المستهدف: إنهاء 4 مهام قبل 5 دقائق من نهاية الوقت.")
