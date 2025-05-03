import streamlit as st

# Заголовок
st.title("Калькулятор ИМТ, ВОО, СЭТ и БЖУ")

# Пол
gender = st.selectbox("Пол", ["Мужской", "Женский"])

# Возраст
age = st.number_input("Возраст", min_value=10, max_value=100, value=25)

# Рост в метрах
height = st.number_input("Рост (м)", min_value=1.0, max_value=2.5, step=0.01, value=1.65)

# Вес в кг
weight = st.number_input("Вес (кг)", min_value=30, max_value=200, step=1, value=55)

# КФА
kfa = st.selectbox("Коэффициент физической активности (КФА)", [1.4, 1.6, 1.8, 2.0])
st.markdown("""
**Как выбрать КФА:**
- **1.4** — сидячий образ жизни (офис, минимум активности)
- **1.6** — лёгкая активность (зарядка, прогулки, 2–3 тренировки/нед.)
- **1.8** — активный образ жизни (4–5 тренировок в неделю)
- **2.0** — высокая активность (спорт каждый день, физическая работа)
""")

# Расчёт ИМТ
bmi = weight / (height ** 2)

if bmi < 18.5:
    bmi_status = "🔴 Недостаточный вес"
elif 18.5 <= bmi <= 24.9:
    bmi_status = "🟢 Норма"
elif 25 <= bmi <= 29.9:
    bmi_status = "🟡 Избыточный вес"
else:
    bmi_status = "🔴 Ожирение"

st.subheader("ИМТ")
st.write(f"Ваш ИМТ: **{bmi:.1f}** — {bmi_status}")

# Расчёт BMR по формуле Миффлина-Сан Жеора
if gender == "Мужской":
    bmr = 10 * weight + 6.25 * (height * 100) - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * (height * 100) - 5 * age - 161

st.subheader("ВОО (Величина основного обмена)")
st.write(f"Ваш ВОО: **{bmr:.0f} ккал/день**")

# Суточная энергозатрата
set = (bmr * kfa)*1.1
st.subheader("Суточная энергетическая потребность (СЭТ)")
st.write(f"Ваш СЭТ: **{set:.0f} ккал/день**")

# Расчёт БЖУ
protein = set * 0.14 / 4  # 1 г белка = 4 ккал
fat = set * 0.30 / 9      # 1 г жира = 9 ккал
carbs = set * 0.56 / 4    # 1 г углеводов = 4 ккал

st.subheader("Рекомендуемое соотношение БЖУ")
st.write(f"Белки (14%): **{protein:.0f} г**")
st.write(f"Жиры (30%): **{fat:.0f} г**")
st.write(f"Углеводы (56%): **{carbs:.0f} г**")
