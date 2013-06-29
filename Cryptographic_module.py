from charm.toolbox.ecgroup import ECGroup
from charm.toolbox.eccurve import prime192v1
from charm.toolbox.ecgroup import ECGroup
#from schemes.pkenc.pkenc_cs98.py import CS98



from charm.toolbox.integergroup import *
from charm.toolbox.PKEnc import *

debug = False
class CS98(PKEnc):	
    def __init__(self):
        global group
        group = IntegerGroup()
           
    def keygen(self, secparam):
        group.paramgen(secparam)
        p = group.p
        g1, g2 = group.randomGen(), group.randomGen()
        
        x1, x2, y1, y2, z = group.random(), group.random(), group.random(), group.random(), group.random()		
        c = ((g1 ** x1) * (g2 ** x2)) % p
        d = ((g1 ** y1) * (g2 ** y2)) % p 
        h = (g1 ** z) % p
		
	# Assemble the public and private keys
        pk = { 'g1' : g1, 'g2' : g2, 'c' : c, 'd' : d, 'h' : h }
        sk = { 'x1' : x1, 'x2' : x2, 'y1' : y1, 'y2' : y2, 'z' : z }
        return (pk, sk)

    def encrypt(self, pk, M):	
        r     = group.random()
        u1    = (pk['g1'] ** r)
        u2    = (pk['g2'] ** r)
        e     = group.encode(M) * (pk['h'] ** r)
        alpha = group.hash(u1, u2, e)
        v     = (pk['c'] ** r) * (pk['d'] ** (r * alpha))		

	# Assemble the ciphertext
        c = { 'u1' : u1, 'u2' : u2, 'e' : e, 'v' : v }
        return c
    
    def decrypt(self, pk, sk, c):	
        alpha = group.hash(c['u1'], c['u2'], c['e'])        
        v_prime = (c['u1'] ** (sk['x1'] + (sk['y1'] * alpha))) * (c['u2'] ** (sk['x2'] + (sk['y2'] * alpha)))
        if not (c['v'] == v_prime):
           return 'ERROR' 

        c['v'].reduce(); v_prime.reduce()
        if debug: print("c['v'] => %s" % c['v'])
        if debug: print("v' => %s" % v_prime)
        return group.decode(c['e'] / (c['u1'] ** sk['z']))













class CS98(PKEnc):
     def __init__(self, curve):
         PKEnc.__init__(self)
         global group
         group = ECGroup(curve)



def keygen(self, secparam):
    g1, g2 = group.random(G), group.random(G)
    x1, x2, y1, y2, z = group.random(ZR), group.random(ZR), group.random(ZR), group.random(ZR), group.random(ZR)
    c = (g1 ** x1) * (g2 ** x2)
    d = (g1 ** y1) * (g2 ** y2)
    h = (g1 ** z)

    pk = { 'g1' : g1, 'g2' : g2, 'c' : c, 'd' : d, 'h' : h, 'H' : group.hash }
    sk = { 'x1' : x1, 'x2' : x2, 'y1' : y1, 'y2' : y2, 'z' : z }
    return (pk, sk)





def encrypt(self, pk, m):
    r   = group.random(ZR)
    u1  = pk['g1'] ** r
    u2  = pk['g2'] ** r
    e   = group.encode(m) * (pk['h'] ** r)
    alpha = pk['H'](u1, u2, e)
    v   = (pk['c'] ** r) * (pk['d'] ** (r * alpha))

    return { 'u1' : u1, 'u2' : u2, 'e' : e, 'v' : v }



def decrypt(self, pk, sk, c):
    alpha = pk['H'](c['u1'], c['u2'], c['e'])

    v_prime = (c['u1'] ** (sk['x1'] + (sk['y1'] * alpha))) * (c['u2'] ** (sk['x2'] + (sk['y2'] * alpha)))
    if (c['v'] != v_prime):
        return 'reject'
    return group.decode(c['e'] / (c['u1'] ** sk['z']))







groupObj = ECGroup(prime192v1)
pkenc = CS98(groupObj)

(pk, sk) = pkenc.keygen()

M = b'Hello World!'
ciphertext = pkenc.encrypt(pk, M)

message = pkenc.decrypt(pk, sk, ciphertext)

