;; Scheme ;;
(define (accumulate combiner start n term)
  (if (= n 0)
      start
      'YOUR-CODE-HERE
  )
)

;;; Tests
(define (identity x) x)
(accumulate * 1 5 identity)
; expect 120

(define (square x) (* x x))
(accumulate + 0 5 square)
; expect 55

(define (how-many-dots s)
  'YOUR-CODE-HERE
)

;;; Tests

(how-many-dots '(1 2 3))
; expect 0
(how-many-dots '(1 2 . 3))
; expect 1
(how-many-dots '((1 . 2) 3 . 4))
; expect 2
(how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
; expect 6
(how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7))))))))
; expect 0



(define (swap s)
  'YOUR-CODE-HERE
)

;;; Tests

(swap (list 1 2 3 4))
; expect (2 1 4 3)
(swap (list 1 2 3 4 5))
; expect (2 1 4 3 5)