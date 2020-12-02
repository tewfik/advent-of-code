;;;; --- Part Two ---
;;;;
;;;; While it appears you validated the passwords correctly, they don't seem
;;;; to be what the Official Toboggan Corporate Authentication System is
;;;; expecting.
;;;;
;;;; The shopkeeper suddenly realizes that he just accidentally explained the
;;;; password policy rules from his old job at the sled rental place down the
;;;; street! The Official Toboggan Corporate Policy actually works a little
;;;; differently.
;;;;
;;;; Each policy actually describes two positions in the password, where 1
;;;; means the first character, 2 means the second character, and so on. (Be
;;;; careful; Toboggan Corporate Policies have no concept of "index zero"!)
;;;; Exactly one of these positions must contain the given letter. Other
;;;; occurrences of the letter are irrelevant for the purposes of policy
;;;; enforcement.
;;;;
;;;; Given the same example list from above:
;;;;
;;;;     1-3 a: abcde is valid: position 1 contains a and position 3 does not.
;;;;     1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
;;;;     2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

(ns part-2-clj.core
  (:require [clojure.string :as str])
  (:gen-class))

(defn parse-bounds [range-str]
  (let [bounds (map #(Integer/parseInt %) (str/split range-str #"-"))]
    [(dec (first bounds)) (dec (second bounds))]))

(defn parse-password-and-policy [password-and-policy]
  {:bounds (parse-bounds (first password-and-policy))
   :letter (first (second password-and-policy))
   :password (last password-and-policy)
   })

(defn parse-input [passwords-and-policies-string]
  (->>
   passwords-and-policies-string
   (#(str/split % #"(\n|: | )"))
   (partition 3)
   (map parse-password-and-policy)))

(defn xor [b1 b2]
  (and
   (or b1 b2)
   (not= b1 b2)))

(defn check-policy [policy]
  (xor (=
        (policy :letter)
        (nth (policy :password) (first (policy :bounds))))
       (=
        (policy :letter)
        (nth (policy :password) (second (policy :bounds))))))

(defn count-respected-policies [policies]
  (count
   (filter check-policy policies)))

(defn -main
  [& args]
  (def passwords-and-policies (parse-input (slurp "resources/input.txt")))
  (count-respected-policies passwords-and-policies))
