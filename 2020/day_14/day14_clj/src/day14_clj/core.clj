(ns day14-clj.core
  (:require [clojure.string :as str])
  (:gen-class))

(defn leftpad-zero [with-char n value]
  (str/replace (format (str "%" n "s") value) #" " with-char))

(defn parse-instruction [instruction-str]
  (let [instruction-raw (str/split instruction-str #" = ")
        value (second instruction-raw)
        verb-key (str/split (first instruction-raw) #"[\[\]]")
        verb (first verb-key)
        maybe-key (when (second verb-key) (Integer/parseInt (second verb-key)))]
    (case verb
      "mem" [:mem
             maybe-key
             (leftpad-zero "0" 36 (Integer/toString (Integer/parseInt value) 2))]
      "mask" [:mask nil value])))

(defn parse-input [input-str]
  (->>
   input-str
   (str/split-lines)
   (map parse-instruction)))

(defn apply-mask [mask value]
  (let [zip (map vector (vec mask) (vec value))]
    (->>
     zip
     (map #(if (= \X (first %))
             (second %)
             (first %)));
     (str/join))))

(defn apply-instruction [acc mask [verb maybe-key value]]
  (case verb
    :mem [(assoc acc maybe-key (apply-mask mask value)) mask]
    :mask [acc value]))

(defn solve-part-1 [instructions]
  (loop [instructions instructions acc {} mask nil]
    (if (empty? instructions)
      (reduce + (map #(Long/parseLong % 2) (vals acc)))
      (let [[new-acc new-mask] (apply-instruction acc mask (first instructions))]
        (recur (rest instructions) new-acc new-mask)))))

(defn -main
  [& args]
  (def instructions (parse-input (slurp "resources/input.txt")))
                                        ;(solve-part-1 instructions)
  instructions
  )
