; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    (else 1)
  )
)

(define (ordered? s)
  'YOUR-CODE-HERE
  (cond
    ((null? (cdr s)) #t)
    ((< (cadr s) (car s)) #f)
    (else (ordered? (cdr s)))
  )
)

(define (nodots s)
  'YOUR-CODE-HERE
  (cond
  ((null? s) nil)
  ((pair? s) (
    if (pair? (car s))
    (cons (nodots (car s)) (nodots (cdr s)))
    (cons (car s) (nodots (cdr s)))))
  (else (cons s nil))
  )
)

; Sets as sorted lists

(define (empty? s) (null? s))

'YOUR-CODE-HERE
(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) #f)
          ((= (car s) v) #t)
          (else (contains? (cdr s) v))
    )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)
'YOUR-CODE-HERE
(define (add s v)
    (cond ((empty? s) (list v))
          ((< (car s) v) (cons (car s) (add (cdr s) v)))
          ((= (car s) v) s)
          (else (cons v s))))
'YOUR-CODE-HERE
(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t)))
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)
'YOUR-CODE-HERE
(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          (else (cons (car t) (union s (cdr t))))
          ))

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
  "YOUR CODE HERE"
  (define (exp_helper b n total)
    (if (= n 0)
     total 
     (exp_helper b (- n 1) (* b total)))
  )
  (exp_helper b n 1)
)

'YOUR-CODE-HERE
(define (filter pred lst)
  (define (filter_helper pred lst result)
    (cond
      ((null? lst) result)
      ((pred (car lst)) (filter_helper pred (cdr lst) (append result (cons (car lst) nil))))
      (else (filter_helper pred (cdr lst) result))
    )
  ) 
  (filter_helper pred lst '()) 
)




