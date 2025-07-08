import pickle

def load_pkl_model():
    try:
        # Update the path to the correct location of the .pkl file
        with open("C:/ELIF/projects/gradproject/handsign_project/handsign_project/handsign_app/xgboost_model.pkl", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model = load_pkl_model()