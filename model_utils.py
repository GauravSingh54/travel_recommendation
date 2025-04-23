import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

df = pd.read_csv('Top Indian Places to Visit.csv')

df = df.drop(columns=['Unnamed: 0', 'Zone', 'Establishment Year', 
                      'Airport with 50km Radius', 'Weekly Off', 
                      'Number of google review in lakhs'], errors='ignore')

label_encoder = {}
for col in ['State', 'City', 'Significance', 'Best Time to visit']:
    le = LabelEncoder()
    df[col + '_enc'] = le.fit_transform(df[col])
    label_encoder[col] = le

features = df[['Significance_enc', 'Best Time to visit_enc']]
kmeans = KMeans(n_clusters=6, init='k-means++', max_iter=300, random_state=42)
df['Cluster'] = kmeans.fit_predict(features)

def predict_cluster(significance, best_time):
    sig_enc = label_encoder['Significance'].transform([significance])[0]
    time_enc = label_encoder['Best Time to visit'].transform([best_time])[0]
    return kmeans.predict([[sig_enc, time_enc]])[0]

def get_recommendations(cluster_id):
    filtered = df[df['Cluster'] == cluster_id]
    # return filtered[['City', 'State', 'Significance', 'Best Time to visit','Name']].to_dict(orient='records')
    return filtered[['Name','City','Entrance Fee in INR','Type','time needed to visit in hrs','Google review rating','DSLR Allowed']].to_dict(orient='records')

def load_data():
    return pd.read_csv("Top Indian Places to Visit.csv")

def get_all_states():
    return sorted(df['State'].unique())

def get_all_significance():
    return sorted(df['Significance'].unique())

def get_all_best_times():
    return sorted(df['Best Time to visit'].unique())

def get_cities_by_state(state):
    df = load_data()
    cities = df[df['State'] == state]['City'].unique().tolist()
    return cities

def get_significance_by_city(city):
    return sorted(df[df['City'] == city]['Significance'].unique())

def get_best_times_by_city(city):
    return sorted(df[df['City'] == city]['Best Time to visit'].unique())