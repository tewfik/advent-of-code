(ns day7-clj.core
  (:require [clojure.string :as str]
            [clojure.set :as set])
  (:gen-class))

(defn join-bag-color [tokens]
  (apply str (interpose " " tokens)))

(defn format-bag [bag-tokens]
  {:color (join-bag-color (take 2 (drop 1 bag-tokens)))
   :quantity (Integer/parseInt (first bag-tokens))})

(defn process-bag-content [tokens]
  "return list of {:color :quantity}"
  (if (= "no" (first tokens))           ; contains no other bags
    []
    (->>
     tokens
     (partition 4)
     (mapv format-bag))))

(defn parse-rule [rule-str]
  "return {color [{:color str :quantity int}]}"
  (let [tokens (str/split rule-str #" ")]
    {(join-bag-color (take 2 tokens)) (process-bag-content (drop 4 tokens))}))

(defn parse-rules [rules-str]
  (->>
   (str/split-lines rules-str)
   (map parse-rule)
   (reduce merge)))

;; (defn solve-part-1 [input]
;;   input)

(declare count-content)
(defn count-bag [rules color]
  (+
   1                                    ; current bag
   (reduce + (count-content rules (rules color)))))

(defn count-content [rules content]
  (->>
   content
   (map #(*
          (% :quantity)
          (count-bag rules (% :color))))))

(defn solve-part-2 [rules]
  (dec                                  ; don't count current bag
   (count-bag rules "shiny gold")))

(defn -main
  [& args]
  (def rules (parse-rules (slurp "resources/input.txt")))

  ;(println "part 1:" (solve-part-1 rules))
  (println "part 2:" (solve-part-2 rules)))
