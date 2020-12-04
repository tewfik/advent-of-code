(ns part-1-2-clj.core
  (:require [clojure.string :as str]
            [clojure.set :as set])
  (:gen-class))

(defn parse-document [document-str]
  (->>
   (str/split document-str #"(\n| |:)")
   (apply hash-map)))

(defn parse-input [input-str]
  (as-> input-str $
    (str/split $ #"\n\n")
    (map parse-document $)))

(defn between [val low high]
  (let [x (Integer/parseInt val)]
    (and
     (>= x low)
     (<= x high))))

(defn check-hgt [hgt]
  (let [groups (re-matches #"(\d{2,3})(cm|in)" hgt)]
    (and
     groups
     (case (nth groups 2)
       "cm" (between (nth groups 1) 150 193)
       "in" (between (nth groups 1) 59 76)
       false))))

(defn enforce-rules [document]
  (and
   (between (document "byr") 1920 2002)
   (between (document "iyr") 2010 2020)
   (between (document "eyr") 2020 2030)
   (check-hgt (document "hgt"))
   (re-matches #"#[0-9a-f]{6}" (document "hcl"))
   (contains? #{"amb" "blu" "brn" "gry" "grn" "hzl" "oth"} (document "ecl"))
   (re-matches #"\d{9}" (document "pid"))))

(defn check-document-part-1 [document]
  (let [required-fields #{"byr" "iyr" "eyr" "hgt" "hcl" "ecl" "pid"}]
    (set/subset? required-fields (set (keys document)))))

(defn check-documents-part-1 [documents]
  (->>
   documents
   (map check-document-part-1)
   (filter identity)
   (count)))

(defn check-document-part-2 [document]
  (let [required-fields #{"byr" "iyr" "eyr" "hgt" "hcl" "ecl" "pid"}]
    (and
     (set/subset? required-fields (set (keys document)))
     (enforce-rules document))))

(defn check-documents-part-2 [documents]
  (->>
   documents
   (map check-document-part-2)
   (filter identity)
   (count)))

(defn -main
  [& args]
  (def input (parse-input (slurp "resources/input.txt")))
  (println (check-documents-part-1 input))
  (println (check-documents-part-2 input)))
