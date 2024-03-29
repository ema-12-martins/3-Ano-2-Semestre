from cryptography import x509
import datetime

def mkpair(x, y):
    """produz uma byte-string contendo o tuplo '(x,y)' ('x' e 'y' são byte-strings)"""
    len_x = len(x)
    len_x_bytes = len_x.to_bytes(2, "little")
    return len_x_bytes + x + y


def unpair(xy):
    """extrai componentes de um par codificado com 'mkpair'"""
    len_x = int.from_bytes(xy[:2], "little")
    x = xy[2 : len_x + 2]
    y = xy[len_x + 2 :]
    return x, y


def cert_load(fname):
    """ lê certificado de ficheiro """
    with open(fname, "rb") as fcert:
        cert = x509.load_pem_x509_certificate(fcert.read())
    return cert


def cert_validtime(cert, now=None):
    """Validate that the current time falls within the validity period of the certificate."""
    if now is None:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
    nowDate = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    if nowDate < cert.not_valid_before or nowDate > cert.not_valid_after:
        raise x509.verification.VerificationError("Certificate is not valid at this time")
    

def cert_validsubject(cert, attrs=[]):
    """ verifica atributos do campo 'subject'. 'attrs'
    é uma lista de pares '(attr,value)' que condiciona
    os valores de 'attr' a 'value'. """
    for attr in attrs:
        if cert.subject.get_attributes_for_oid(attr[0])[0].value != attr[1]:
            raise x509.verification.VerificationError("Certificate subject does not match expected value")
        

def verify_directly_issued_by(ca_cert, cert):    
    return ca_cert.subject == cert.issuer
    

def valida_certServidor(ca_cert,serv_cert):
    try:
        verify_directly_issued_by(ca_cert,serv_cert)
        cert_validtime(serv_cert)
        cert_validsubject(serv_cert, [(x509.NameOID.COMMON_NAME, "SSI Message Relay Server")])
        return True
    except Exception as e:
        print(e)
        return False
    

def valida_certCliente(ca_cert,client_cert):
    try:
        verify_directly_issued_by(ca_cert,client_cert)
        cert_validtime(client_cert)
        cert_validsubject(client_cert, [(x509.NameOID.COMMON_NAME, "User 1 (SSI MSG Relay Client 1)")])
        return True
    except Exception as e:
        print(e)
        return False