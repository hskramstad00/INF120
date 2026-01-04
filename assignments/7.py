# Assignment 7
# Skal lage en funskjon som analyserer bruk av paranteser i tekst(strenger)
# Funksjonen skal sjekke 3 forskjellige ting om bruk av paranteser
# 1. Maksimal dybde for parantesene (mad_depth). Hvor mange paranteser inne i hverandre?
# 2. Gyldig bruk av paranteser (is_valid). Er det en lukke parantes som ikke matcher en åpen parantes.
# 3. Er alle paranteser balanserte (is_balanced). Finnes det lukke parantese for alle åpne paranteser

lisp = '''
(defun LaTeX-newline ()
  "Start a new line potentially staying within comments.
This depends on `LaTeX-insert-into-comments'."
  (interactive)
  (if LaTeX-insert-into-comments
      (cond ((and (save-excursion (skip-chars-backward " \t") (bolp))
                  (save-excursion
                    (skip-chars-forward " \t")
                    (looking-at (concat TeX-comment-start-regexp "+"))))
             (beginning-of-line)
             (insert (buffer-substring-no-properties
                      (line-beginning-position) (match-end 0)))
             (newline))
            ((and (not (bolp))
                  (save-excursion
                    (skip-chars-forward " \t") (not (TeX-escaped-p)))
                  (looking-at
                   (concat "[ \t]*" TeX-comment-start-regexp "+[ \t]*")))
             (delete-region (match-beginning 0) (match-end 0))
             (indent-new-comment-line))
            ;; `indent-new-comment-line' does nothing when
            ;; `comment-auto-fill-only-comments' is non-nil, so we
            ;; must be sure to be in a comment before calling it.  In
            ;; any other case `newline' is used.
            ((TeX-in-comment)
             (indent-new-comment-line))
            (t
             (newline)))
    (newline)))
'''

def check_parantheses(text):
    open_list = ["[","{","(",]
    close_list = ["]","}",")"]
    check = []
    telle = []
    max_depth = 0
    is_valid = True
    is_balanced = False

    for i in text:
        if i in open_list:
            check.append(1)
        
        elif i in close_list:
            check.append(-1)

        telle.append(sum(check))

    if sum(check) < 0:
        is_valid = False
        
    if sum(check) == 0:
        is_balanced = True

    max_depth = max(telle)
    print(check)
    return max_depth, is_valid, is_balanced
    
res = check_parantheses(lisp)

print(f'max depth: {res[0]}, valid: {res[1]}, balanced: {res[2]}')