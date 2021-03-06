import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from extract_statistics import extract_basic
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import xgboost as xgb
from sklearn.feature_selection import RFE
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd, time
from extract_statistics import *

np.random.seed(0)
patient = 'FAC001'


def make_preprocessed_data():
	print('old code... doesnt work anymore!!! use: "from load_raw import load_raw" to get the data!')
	return
	global av_mem, feature_names_mem, y_mem, feature_names_perc, av_perc, y_perc
	dt_p, dt_m, X_mem, y_mem, X_perc, y_perc = pickle.load(open('preprocessed/{}.pkl'.format(patient), 'rb'))

	y_mem = y_mem.T.flatten()
	y_perc = y_perc.T.flatten()

	av_mem, feature_names_mem = extract_basic(X_mem)
	av_perc, feature_names_perc = extract_basic(X_perc)

	with open('preprocessed/features{}.pkl'.format(patient), 'wb') as fp:
		pickle.dump([av_mem, feature_names_mem, av_perc, feature_names_perc, y_mem, y_perc], fp)


def load_preprocessed_data():
	global av_mem, feature_names_mem, y_mem, feature_names_perc, av_perc, y_perc
	with open('preprocessed/features{}.pkl'.format(patient), 'rb') as f:
		av_mem, feature_names_mem, av_perc, feature_names_perc, y_mem, y_perc = pickle.load(f)


def knn():
	knn = KNeighborsClassifier(n_jobs=-1)
	parameters = {'leaf_size': np.arange(15, 45, 5), 'n_neighbors': np.arange(2, 25, 1)}
	clf = GridSearchCV(knn, parameters)
	# clf.fit(av_mem, y_mem)
	# print(clf.cv_results_)


# print('mem:', cross_val_score(knn, av_mem, y_mem, cv=3))
# knn = KNeighborsClassifier()
# print('perc:', cross_val_score(knn, av_perc, y_perc, cv=3))


def random_forest():
	rf = RandomForestClassifier()
	# print('mem:', cross_val_score(rf, av_mem, y_mem, cv=3))
	# rf = RandomForestClassifier()
	# print('perc:', cross_val_score(rf, av_perc, y_perc, cv=3))


def svm():
	svm = SVC()
	# print('mem:', cross_val_score(svm, av_mem, y_mem, cv=3))
	# svm = SVC()
	# print('prec:', cross_val_score(svm, av_perc, y_perc, cv=3))


def mlp():
	mlp = MLPClassifier()
	# print('mem:', cross_val_score(mlp, av_mem, y_mem, cv=3))
	# mlp = MLPClassifier()
	# print('perc:', cross_val_score(mlp, av_perc, y_perc, cv=3))


def xgboost():
	print('TODO: FIX THIS CODE -> old code... doesnt work anymore!!!')
	return
	################
	## W-I-P Cedric
	# feat_info = input("Would you like to get feature info? (y/n) ")
	#
	# if feat_info == 'y':
	# 	gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.01)
	#
	# 	print("Perception...")
	# 	selector = RFE(gbm, step=100, verbose=2)
	# 	# selector.fit(av_perc, y_perc)
	# 	feats = selector.support_
	# 	feats_ind = [i for i, x in enumerate(feats) if x]
	# 	selected_features = [feature_names_perc[i] for i in (feats_ind)]
	# 	lead_freq = [s[-3:] for s in selected_features]
	# 	lead_freq = [s.replace('_', '') for s in lead_freq]
	# 	lead_freq = [int(s.replace('d', '')) for s in lead_freq]
	# 	counts = Counter(np.sort(lead_freq))
	# 	leads = set(lead_freq)
	# 	# freq = [len(lead_freq) for key, group in groupby(lead_freq)]
	# 	plt.bar(counts.keys(), counts.values())
	# 	plt.ion()
	# 	plt.title("Perception")
	# 	plt.show()
	# 	av_perc = selector.transform(av_perc)
	#
	# 	print("Memory...")
	# 	gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.01)
	# 	selector = RFE(gbm, step=100, verbose=2)
	# 	selector.fit(av_mem, y_mem)
	# 	feats = selector.support_
	# 	feats_ind = [i for i, x in enumerate(feats) if x]
	# 	selected_features = [feature_names_perc[i] for i in (feats_ind)]
	# 	lead_freq = [s[-3:] for s in selected_features]
	# 	lead_freq = [s.replace('_', '') for s in lead_freq]
	# 	lead_freq = [int(s.replace('d', '')) for s in lead_freq]
	# 	counts = Counter(np.sort(lead_freq))
	# 	leads = set(lead_freq)
	# 	# freq = [len(lead_freq) for key, group in groupby(lead_freq)]
	# 	plt.bar(counts.keys(), counts.values())
	# 	plt.ion()
	# 	plt.title("Memory")
	# 	plt.show()
	# 	av_mem = selector.transform(av_mem)
	#
	# 	gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.01)
	# 	print('perc:', cross_val_score(gbm, av_perc, y_perc, cv=3))
	# 	gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.01)
	# 	print('mem:', cross_val_score(gbm, av_mem, y_mem, cv=3))
	#
	# else:
	# 	gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.01)
	# 	print('mem:', cross_val_score(gbm, av_mem, y_mem, cv=3))
	#
	# 	gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.01)
	# 	print('perc:', cross_val_score(gbm, av_perc, y_perc, cv=3))


def main():
	from load_raw import load_raw
	patient_data = load_raw('raw_FAC002')
	'''
			patient_data = contains all the data for patient X

			patient_data['eeg_m'] = all the memory eeg leads shape = L leads by T trials by D data points
			patient_data['eeg_p'] = all the perc eeg leads shape = L leads by T trials by D data points

			patient_data['simVecM'] # all the memory y values shape = T trials
			patient_data['simVecP'] # all the perception y values shape = T trials
	'''
	t = time.time()
	for trial in range(patient_data['eeg_m'].shape[1]):
		for lead in range(patient_data['eeg_m'].shape[0]):
			signal = patient_data['eeg_m'][lead][trial]
			vertices, signal_smooth = create_vertex2vertex(signal, spacing=10)
			cuvv_nm_std_cov(signal_smooth, vertices)
	print(time.time()-t)
			# plt.plot(signal)
		# 	plt.plot(signal_smooth)
		# 	plt.plot(vertices, signal_smooth[vertices], 'ro')
		# plt.show()


if __name__ == '__main__':
	main()
