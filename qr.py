import urllib.request

    
# plantilla de la vcard:
VCARD_TEMPLATE = """
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s
ORG:Transelca
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;3800 Zanker Rd;San Jose;CA;95134;Valledupar
EMAIL;PREF;INTERNET:%s
END:VCARD
"""
##llamado de la api
QR_CODE_TEMPLATE = "http://api.qrserver.com/v1/create-qr-code/?data=%s&size=300x300"
## Excel
filename = "data/raisin_team.csv"

try:
    file_hdl = open(filename)
#Creacion de tarjeta vcf
    for each_line in file_hdl:
        data = each_line.strip('\n').split(',')
        last_name, first_name, title, email, phone_number = data
        full_name = first_name + ' ' + last_name
        vcard = VCARD_TEMPLATE % (last_name, first_name,
                                  full_name,
                                  title,
                                  phone_number,
                                  email)

        
        out_filename = '.'.join(["data/" + first_name + '-' + last_name, "vcf"])
        out_file_hdl = open(out_filename, 'w')
        out_file_hdl.write(vcard)
        out_file_hdl.close()
        
        #comienza la creacion de qr
        
        vcard_url = QR_CODE_TEMPLATE % (vcard)
        cnxn = urllib.urlopen(vcard_url)
        qr_code = cnxn.read()
        cnxn.close()
        qr_filename = '.'.join(["data/" + first_name + '-' + last_name, "png"])
        with open(qr_filename, 'w') as qr_file_hdl:
            qr_file_hdl.write(qr_code)
        print "Created QR-code %s file." %(qr_filename)


           ## En caso de un error se imprime 
except Exception as error:
    print str(error)