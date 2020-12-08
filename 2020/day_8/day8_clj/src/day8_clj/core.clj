(ns day8-clj.core
  (:require [clojure.string :as str])
  (:gen-class))

(defn parse-instructions [instructions-str]
  (->>
   instructions-str
   (str/split-lines)
   (mapv #(let [tokens (str/split % #" ")]
           [(first tokens)
            (Integer/parseInt (second tokens))]))))

(defn run [instructions visited acc point]
  (if (nil? (get instructions point))
    [:success acc] ; out of infinite loop
    (let [current-instruction (nth instructions point)
          [verb value] current-instruction]
      (if (contains? visited point)
        [:infinite-loop acc] ; infinite loop
        (case verb
          "nop" (run instructions (conj visited point) acc (inc point))
          "acc" (run instructions (conj visited point) (+ acc value) (inc point))
          "jmp" (run instructions (conj visited point) acc (+ point value)))))))

(defn toggle [instruction]
  [(case (first instruction)
     "nop" "jmp"
     "jmp" "nop"
     "acc" "acc")
   (second instruction)])

(defn alter-instructions [instructions idx]
  (assoc instructions idx (toggle (get instructions idx))))

(defn solve-part-2 [instructions]
  (->>
   (range (count instructions))
   (map #(run (alter-instructions instructions %) #{} 0 0))
   (filter #(= :success (first %)))
   (first)))

(defn solve-part-1 [instructions]
  (run instructions #{} 0 0))

(defn -main
  [& args]
  (def instructions (parse-instructions (slurp "resources/input.txt")))

  (println "part 1: " (solve-part-1 instructions))
  (println "part 2: " (solve-part-2 instructions)))
