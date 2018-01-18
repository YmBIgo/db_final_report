#coding:utf-8

# from get_page import GetPage

import downloader

# g = GetPage()
# g.connect("https://www.youtube.com/watch?v=xY-XmGEcpTM")
# g.scroll_to_bottom(10, 500)
# content = g.get_content().encode('utf-8')
# # ytd-comment-thread-renderer.style-scope:nth-child(1) > ytd-comment-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ytd-expander:nth-child(2) > div:nth-child(1) > yt-formatted-string:nth-child(2)
# # comments = g.select_css('.ytd-item-section-renderer > .ytd-expander > .ytd-comment-renderer')
# # print comments
# f = open("data/youtube_data.html", 'w')
# f.write(content)
# f.close()
# g.finish()

download_urls = ["czBa9nbvGNA", "snxb_PSe3Ps", "D4zBVD0sL7Y", "H75kyGItXFo", "lYGGpc2mMno", "65_PmYipnpk", "mB2V0BXH608", "F9GujgK0y2M", "mElVGah7Epg", "Q6NiqRqGePU", "AZnymkpsCH0", "ZM_I2uwOfXw", "jjfIwaRgRds", "Qk7pPutimCM", "l_zaV7HnsLA", "QNmIWEqb3sM", "UzxYlbK2c7E", "Z-mo_P9DkuA", "DH4m49kyVYo", "bzb4W_y4s9E", "xUNmzLKvdm4", "Dugn51K_6WA", "8bepzUM1x3w", "5phijpb1Hjk", "19uLJdelYck", "ZyYqyYAKGC0", "9g3O-G7EGbk", "IK1Pjgix79k", "UbnfcUxD6j4", "tpNgf5a34as"]
download_urls = ["OoI57NeMwCc"]
print len(download_urls)

for v_id in download_urls:
	vurl_o = "data/youtube/{}.json".format(v_id)
	# downloader.downloader(v_id, vurl_o)

	# fixed_vurl_o = "data/youtube1/{}.json".format(v_id)
	# r_array = []
	# r_f = open(vurl_o, "r")
	# for line in r_f:
	# 	r_array.append(line.strip() + ",\n")
	# 	# print line
	# r_f.close()
	# print r_array
	# w_f = open(fixed_vurl_o, "w")
	# w_f.write(''.join(r_array))
	# w_f.close()
