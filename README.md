
---

This repository contains the **final deployment** code for **QuestBo-T**, a project that uses Retrieval-Augmented Generation (RAG) combined with Large Language Models (LLMs) to answer subject-specific questions from **Physics**, **Chemistry**, and **Biology**.

---

## 🔥 What This Project Does

- Takes user questions related to **Physics**, **Chemistry**, or **Biology**.
- Uses a **retrieval system** to fetch relevant documents or context from a knowledge base.
- Feeds the retrieved context + question into a **Large Language Model (LLM) {GEMINI}** to generate accurate answers.
- Designed to help students and learners get precise, subject-based answers.

---

## 🛠️ Technologies Used

- **Python** 🐍
- **Hugging Face Transformers** 🤗 (for using LLMs)
- **FAISS** (for fast similarity search and retrieval)
- **Streamlit** (for serving the app)
- **PyTorch** (for model inference)
- **Pandas** & **NumPy** (for data handling)

---

## 🔄 Project Flow (How It Works)

### 📊 Flow Diagram

```
[ User Question ] 
        ⬇️
[ Text Embedding Model ] 
        ⬇️
[ FAISS Retriever ➡️ Finds Relevant Docs ]
        ⬇️
[ Combine Question + Retrieved Docs ]
        ⬇️
[ Large Language Model (LLM) ➡️ Generates Answer ]
        ⬇️
[ Display Answer to User ]
```

---

## 📂 Code Structure

```
final deployment/
├── app.py          # Main file to run the app
├── config/         # Configuration files
├── models/         # Pre-trained models and pipelines
├── utils/          # Helper functions (retrieval, preprocessing, etc.)
└── requirements.txt
```

---

## ✅ Steps to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/liyakhathshaik/questbo-t.git
    cd questbo-t/py,ch,bi,ragllm/final deployment
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    python app.py
    ```

---

## 🧪 Example Subjects Supported

- ⚛️ Physics (e.g., "Explain Newton's second law")
- 🧪 Chemistry (e.g., "What is covalent bonding?")
- 🔬 Biology (e.g., "Stages of cellular respiration")

---

---

## ✅ Steps to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/liyakhathshaik/questbo-t.git
    cd questbo-t/py,ch,bi,ragllm/final deployment
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    python app.py
    ```

---

## 🧪 Example Subjects Supported

- ⚛️ Physics (e.g., "Explain Newton's second law")
- 🧪 Chemistry (e.g., "What is covalent bonding?")
- 🔬 Biology (e.g., "Stages of cellular respiration")

---

## 📈 Results & Advantages

### 🚀 Why QuestBo-T (RAG Model) is Better for IIT JEE Questions

- ✅ **Syllabus-Specific Context**:  
  QuestBo-T retrieves context **only from documents aligned with the IIT JEE syllabus**, ensuring that answers stay relevant and on-topic.  
  General AI models like ChatGPT may pull in broader knowledge that sometimes goes outside syllabus scope — which can confuse students.

- ✅ **Higher Accuracy in Subject Questions**:  
  When tested on IIT JEE previous year questions:
  - QuestBo-T generated more accurate and syllabus-specific answers compared to general-purpose AI.
  - Retrieval step ensures that even complex, multi-step problems get supporting context before answer generation.

- ✅ **Focused for Education**:  
  This model is fine-tuned to perform well on academic-style queries, unlike general models that are trained for open-domain conversation.

### 📊 Example Result Comparison

| Question                              | General AI Answer                   | QuestBo-T Answer (with RAG)            |
|---------------------------------------|-------------------------------------|---------------------------------------|
| "Explain Bohr’s postulates"           | General explanation with extra info | Focused explanation matching NCERT & IIT syllabus |
| "Derive Newton's second law formula"  | Mixed explanation                   | Step-by-step syllabus-based derivation |

### 🏅 Best Use Case:
- Perfect for **IIT JEE** aspirants and academic platforms needing **syllabus-locked** question answering.
- Generates practice questions or explanations based on the **retrieved syllabus content** — improving learning accuracy.

---


## 🙌 Author

Developed by [liyakhathshaik](https://github.com/liyakhathshaik)

---

```

---
