pip install kaggle
mkdir ~/.kaggle
mv /path/to/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# download_dataset.sh
kaggle datasets download -d rohitmahulkar/online-retails-sale-dataset
unzip online-retails-sale-dataset.zip -d dataset

bash download_dataset.sh
