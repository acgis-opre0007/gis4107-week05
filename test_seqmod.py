import seqmod
seq = "ABCD"

def test_seqmod(seq,skip_index=None,truncate_index=None):
    return seqmod.mod_sequence(seq,skip_index,truncate_index)

print(f'\nExpected: ABCD\nActual: {test_seqmod(seq)}\n')
print(f'\nExpected: BCD\nActual: {test_seqmod(seq,0)}\n')
print(f'\nExpected: ACD\nActual: {test_seqmod(seq,1)}\n')
print(f'\nExpected: A\nActual: {test_seqmod(seq,1,2)}\n')
print(f'\nExpected: AB\nActual: {test_seqmod(seq,2,2)}\n')
print(f'\nExpected: AB\nActual: {test_seqmod(seq,3,2)}\n')
print(f'\nExpected: ABCD\nActual: {test_seqmod(seq,4,None)}\n')
print(f'\nExpected: ABCD\nActual: {test_seqmod(seq,None,4)}\n')
print(f'\nExpected: ACD\nActual: {test_seqmod(seq,1,4)}\n')