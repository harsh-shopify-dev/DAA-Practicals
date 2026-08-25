import time

def b_sort(a):
    for i in range(len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def s_sort(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[m] > a[j]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a

def i_sort(a):
    for i in range(1, len(a)):
        k = a[i]
        j = i-1
        while j >= 0 and k < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k
    return a

def m_sort(a):
    if len(a) > 1:
        mid = len(a)//2
        l, r = a[:mid], a[mid:]
        m_sort(l)
        m_sort(r)
        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k] = l[i]; i+=1
            else:
                a[k] = r[j]; j+=1
            k+=1
        while i < len(l):
            a[k] = l[i]; i+=1; k+=1
        while j < len(r):
            a[k] = r[j]; j+=1; k+=1
    return a

def q_sort(a):
    if len(a) <= 1: return a
    p = a[len(a)//2]
    return q_sort([x for x in a if x < p]) + [x for x in a if x == p] + q_sort([x for x in a if x > p])

d = [64, 34, 25, 12, 22, 11, 90]
for n, f in [("Bubble", b_sort), ("Selection", s_sort), ("Insertion", i_sort), ("Merge", m_sort), ("Quick", q_sort)]:
    t = time.time()
    f(d.copy())
    print(n, time.time()-t)
