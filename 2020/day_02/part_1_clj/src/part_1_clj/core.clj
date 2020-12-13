;;;; --- Day 2: Password Philosophy ---
;;;;
;;;; Your flight departs in a few days from the coastal airport; the easiest
;;;; way down to the coast from here is via toboggan.
;;;;
;;;; The shopkeeper at the North Pole Toboggan Rental Shop is having a bad
;;;; day. "Something's wrong with our computers; we can't log in!" You ask if
;;;; you can take a look.
;;;;
;;;; Their password database seems to be a little corrupted: some of the
;;;; passwords wouldn't have been allowed by the Official Toboggan Corporate
;;;; Policy that was in effect when they were chosen.
;;;;
;;;; To try to debug the problem, they have created a list (your puzzle input)
;;;; of passwords (according to the corrupted database) and the corporate
;;;; policy when that password was set.
;;;;
;;;; For example, suppose you have the following list:
;;;;
;;;; 1-3 a: abcde
;;;; 1-3 b: cdefg
;;;; 2-9 c: ccccccccc
;;;;
;;;; Each line gives the password policy and then the password. The password
;;;; policy indicates the lowest and highest number of times a given letter
;;;; must appear for the password to be valid. For example, 1-3 a means that
;;;; the password must contain a at least 1 time and at most 3 times.
;;;;
;;;; In the above example, 2 passwords are valid. The middle password, cdefg,
;;;; is not; it contains no instances of b, but needs at least 1. The first
;;;; and third passwords are valid: they contain one a or nine c, both within
;;;; the limits of their respective policies.
;;;;
;;;; How many passwords are valid according to their policies?
;;;;
;;;; Your puzzle answer was 500.

(ns part-1-clj.core
  (:require [clojure.string :as str])
  (:gen-class))

(defn parse-range [range-str]
  (let [bounds (map #(Integer/parseInt %) (str/split range-str #"-"))]
    (set
     (range (first bounds) (inc (second bounds))))))

(defn parse-password-and-policy [password-and-policy]
  {:range (parse-range (first password-and-policy))
   :letter (first (second password-and-policy))
   :password (last password-and-policy)
   })

(defn parse-input [passwords-and-policies-string]
  (->>
   passwords-and-policies-string
   (#(str/split % #"(\n|: | )"))
   (partition 3)
   (map parse-password-and-policy)))

(defn check-policy [policy]
  (->>
   (policy :password)
   (filter #{(policy :letter)})
   (count)
   (contains? (policy :range))))

(defn count-respected-policies [policies]
  (count
   (filter check-policy policies)))

(defn -main
  [& args]
  (def passwords-and-policies (parse-input (slurp "resources/input.txt")))
  (count-respected-policies passwords-and-policies))
