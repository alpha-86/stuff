import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
save_file = sys.argv[3]


file1= open(file1, 'r')
pac1 = file1.read()
file1.close()

file2 = open(file2, 'r')
pac2 = file2.read()
file2.close()


pac1 = pac1.replace('FindProxyForURL', 'FindProxyForURL_pac1')
pac2 = pac2.replace('FindProxyForURL', 'FindProxyForURL_pac2')

func = """
function FindProxyForURL(url, host) {
	var pac1 = FindProxyForURL_pac1(url, host)
	if (pac1 != "DIRECT") {
		return pac1
	}
    var pac2 = FindProxyForURL_pac2(url, host)
    if (pac2 != "DIRECT") {
        return pac2
    }
    return "DIRECT";
}
"""
pac = pac1+pac2+func

save_file = open(save_file, 'w')
save_file.write(pac)
save_file.close()

