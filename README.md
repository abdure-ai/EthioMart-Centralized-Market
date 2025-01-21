# EthioMart Named Entity Recognition (NER) System

## **Overview**
EthioMart’s NER system is designed to extract structured information such as product names, prices, locations, and contact details from Amharic Telegram messages. This project leverages data preparation, annotation, and fine-tuned transformer models to enhance EthioMart’s centralized e-commerce platform.

---

## **Features**
- **Real-time Data Collection**: Scrapes and processes messages from Ethiopian-based Telegram e-commerce channels.
- **Named Entity Recognition (NER)**: Identifies key entities like products, prices, and locations.
- **Pre-trained Models**: Fine-tunes multilingual and African-specific transformer models (e.g., XLM-Roberta, AfroXLM-R).
- **Structured Output**: Generates structured datasets for integration with EthioMart’s platform.

---

## **Project Workflow**

### **1. Data Preparation**
- **Data Collection**:
  - Telegram messages collected using the Telethon library.
  - Metadata such as sender, timestamp, and media details included.
- **Preprocessing**:
  - Cleaned and normalized Amharic text (e.g., removed emojis, repetitive characters).
  - Tokenized text for further annotation and analysis.
- **Output**: Structured dataset saved as `structured_messages.csv`.

### **2. Data Annotation**
- Annotated key entities in CoNLL format:
  - `B-Product`, `I-Product` for product names.
  - `B-Price`, `I-Price` for prices.
  - `B-LOC`, `I-LOC` for locations.
  - `O` for non-entity tokens.
- **Output**: Annotated dataset saved as `labeled_dataset.conll`.

### **3. Model Fine-Tuning**
- **Models Used**:
  - `XLM-Roberta`: Multilingual transformer.
  - `AfroXLM-R`: Optimized for African languages.
  - `bert-tiny-amharic`: Lightweight model for faster inference.
- **Evaluation Metrics**:
  - Precision, Recall, F1-Score, and Inference Speed.
- **Results**:
  - XLM-Roberta achieved the highest F1-Score (0.91) and was selected for production.

### **4. Deployment**
- Plans to integrate the NER system into EthioMart’s platform via a REST API.
- Fine-tuned model saved in `fine_tuned_model/` directory.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/abdure-ai/EthioMart-Centralized-Market.git
cd ethio_mart_ner
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Prepare Data**
- Ensure `structured_messages.csv` and `labeled_dataset.conll` are in the project directory.
- Update `.gitignore` to exclude `venv/` and `data/` directories.

### **4. Fine-Tune Models**
Run the fine-tuning script for NER:
```bash
python fine_tune_ner.py
```

### **5. Evaluate Models**
Evaluate the fine-tuned models:
```bash
python evaluate_ner.py
```

---

## **Project Structure**
```plaintext
.
├── data/                   # Raw and preprocessed data
├── models/                 # Saved fine-tuned models
├── scripts/                # Scripts for preprocessing, fine-tuning, and evaluation
├── structured_messages.csv # Structured dataset
├── labeled_dataset.conll   # Annotated dataset
├── fine_tune_ner.py        # Fine-tuning script
├── evaluate_ner.py         # Evaluation script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore rules
```

---

## **Deliverables**
- `structured_messages.csv`: Preprocessed dataset.
- `labeled_dataset.conll`: Annotated dataset in CoNLL format.
- `fine_tuned_model/`: Directory containing the best-performing model.
- Evaluation results summarized in the [Final Report](final_submission_report.pdf).

---

## **Future Work**
1. Expand the dataset by collecting messages from additional Telegram channels.
2. Explore semi-supervised learning for scalable annotation.
3. Integrate OCR capabilities to analyze product images.
4. Deploy the NER system as a production-ready REST API.

---

## **License**
This project is licensed under the MIT License.

---

## **Contact**
For inquiries, please contact:
**Abdurezak**  
Email: [abdurewzebtu143.com]  
GitHub: [(https://github.com/abdure-ai/EthioMart-Centralized-Market)]
