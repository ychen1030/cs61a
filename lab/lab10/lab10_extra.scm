;; Extra Scheme Questions ;;

; Q6
(define (remove item lst)
  (cond
  	((null? lst) nil)
  	((= item (car lst)) (remove item (cdr lst)))
  	(else (cons (car lst) (remove item (cdr lst)))))
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q7
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
	(if (> b a) (gcd b a)
		(cond
			((= b 1) 1)
			((= b 0) a)
			((= (modulo a b) 0) b)
	  		(else (gcd b (modulo a b)))))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (split-at lst n)
	(cond
		((= n 0) (cons nil lst))
		((null? lst) (cons lst nil))
		(else (let ((rec (split-at (cdr lst) (- n 1)))) (cons (cons (car lst) (car rec)) (cdr rec)))))
)






