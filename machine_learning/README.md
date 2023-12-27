
## Machine Learning Module: Logistic Regression

### Overview
This module implements a Logistic Regression model for classifying astronomical objects in spectrum data, providing a crucial tool for astrophysical analysis.

### Features
- **Data Preparation**: Generates and preprocesses data for the machine learning model.
- **Model Training**: Includes functionalities to train the Logistic Regression model on the prepared data.
- **Predictions and Evaluation**: Facilitates making predictions and evaluating the model using confusion matrices.

### Usage

#### Setting Up
Install `sklearn`, `pandas`, and ensure `data_extraction` and `metadata_extraction` modules are available.

#### MachineLearning Class
1. **Initialization**:
   ```python
   from machine_learning import MachineLearning
   ml = MachineLearning()
   ```

2. **Data Generation**:
   ```python
   ml.generate_ml_data()
   ```

3. **Train-Test Split**:
   ```python
   ml.train_test_split()
   ```

4. **Training the Model**:
   ```python
   ml.fit()
   ```

5. **Making Predictions**:
   - For direct predictions: `ml.predict(X)`
   - For prediction probabilities: `ml.predict_proba(X)`

6. **Model Evaluation**:
   ```python
   y_pred = ml.predict(ml.X_test)
   confusion_matrix = ml.generate_confusion_matrix(ml.y_test, y_pred)
   ```

### Example
```python
ml = MachineLearning()
ml.generate_ml_data()
ml.train_test_split()
ml.fit()
y_pred = ml.predict(ml.X_test)
confusion_matrix = ml.generate_confusion_matrix(ml.y_test, y_pred)
```

### Integration
This module can be seamlessly integrated with Data Extraction and Metadata Extraction modules, enhancing the analytical capabilities in astrophysical research.

### Conclusion
The Machine Learning module with Logistic Regression provides a robust tool for the classification of astronomical objects, aiding in the deeper understanding of astrophysical phenomena.