import json
import csv

def get_data(d_id):
	file_path = "data/feeling_result/{}.json".format(d_id)
	f = open(file_path, "r")
	j_r = json.load(f)
	feeling_result = {}
	for j_v in j_r.values():
		for j_v_ele in j_v:
			if (j_v[j_v_ele][0] in feeling_result) == False:
				feeling_result[j_v[j_v_ele][0]] = [j_v[j_v_ele][1], j_v[j_v_ele][2]]
			else:
				feeling_result[j_v[j_v_ele][0]][0] += j_v[j_v_ele][1]
	return feeling_result

def collect_feeling_data():
	file_path = "data/feeling_grouping2/result.json"
	f = open(file_path, "r")
	j_r = json.load(f)
	feeling_results = {}
	feeling_num_results = {}
	for j_r_ele in j_r:
		# feeling_results[j_r_ele] = {"AFRAID":0, "ALIVE":0, "ANGRY":0, "CONFUSED":0, "DEPRESSED":0, "GOOD":0, "HAPPY":0, "HELPNESS":0, "HURT":0, "INDIFFERENT":0, "INTERESTED":0, "LOVE":0, "OPEN":0, "POSITIVE":0, "SAD":0, "STRONG":0}
		feeling_results[j_r_ele] = {}
		for j_r_ele_k in j_r[j_r_ele]:
			j_r_ele_v = j_r[j_r_ele][j_r_ele_k]
			print j_r_ele_v[0], j_r_ele_v[1]
			if (j_r_ele_v[1] in feeling_results[j_r_ele]) == False:
				feeling_results[j_r_ele][j_r_ele_v[1]] = j_r_ele_v[0]
			else:
				feeling_results[j_r_ele][j_r_ele_v[1]] += j_r_ele_v[0]
			# if (j_r_ele_v[1] in feeling_results[j_r_ele]) == True:
			# 	feeling_results[j_r_ele][j_r_ele_v[1]] = j_r_ele_v[0]
			# else:
			# 	feeling_results[j_r_ele][j_r_ele_v[1]] += j_r_ele_v[0]

	for f_u in feeling_results:
		feeling_category_str = ""
		feeling_categies = feeling_results[f_u]
		for feeling_category in feeling_categies:
			feeling_category_str += feeling_category + ", "
		print f_u
		print feeling_category_str

	# 	feeling_num_result = []
	# 	for str_num in feeling_results[j_r_ele]:
	# 		feeling_num_result.append(feeling_results[j_r_ele][str_num])
	# 	feeling_num_results[j_r_ele] = feeling_num_result
	# f = open("data/feeling_grouping2/feeling_num_result3.json", "w")
	# json.dump(feeling_num_results, f, indent=2)
	# f.close()

def gen_json(dict):
	f = open("data/feeling_grouping2/result.json", "w")
	json.dump(dict, f, indent=2)
	f.close()

def gen_csv():
	f = open("data/feeling_grouping2/feeling_num_result1.json", "r")
	j_r = json.load(f)
	print j_r
	csv_f = open("data/feeling_grouping2/feeling_results.csv", "wb")
	writer = csv.DictWriter(csv_f, j_r.keys())
	writer.writeheader()
	writer.writerow(j_r)
	csv_f.close()
	f.close()

# download_urls = ["czBa9nbvGNA", "snxb_PSe3Ps", "D4zBVD0sL7Y", "H75kyGItXFo", "lYGGpc2mMno", "65_PmYipnpk", "mB2V0BXH608", "F9GujgK0y2M", "mElVGah7Epg", "Q6NiqRqGePU", "AZnymkpsCH0", "ZM_I2uwOfXw", "jjfIwaRgRds", "Qk7pPutimCM", "l_zaV7HnsLA", "QNmIWEqb3sM", "UzxYlbK2c7E", "Z-mo_P9DkuA", "DH4m49kyVYo", "bzb4W_y4s9E", "xUNmzLKvdm4", "Dugn51K_6WA", "8bepzUM1x3w", "5phijpb1Hjk", "19uLJdelYck", "ZyYqyYAKGC0", "9g3O-G7EGbk", "IK1Pjgix79k", "UbnfcUxD6j4", "tpNgf5a34as"]
# download_urls = ["czBa9nbvGNA"]
# download_results = {}
# for d_id in download_urls:
# 	download_result = get_data(d_id)
# 	download_results[d_id] = download_result
# 	print download_results
# gen_json(download_results)

collect_feeling_data()
# gen_csv()
