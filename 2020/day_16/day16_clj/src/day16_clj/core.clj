(ns day16-clj.core
  (:require [clojure.string :as str]
            [clojure.set :as set])
  (:gen-class))


(defn parse-ticket [ticket-str]
  (as-> ticket-str $
    (str/split $ #",")
    (map #(Integer/parseInt %) $)))

(defn parse-rule [rule-str]
  (let [[field raw-values] (str/split rule-str #": ")
        values (as-> raw-values $
                 (str/split $ #"( or |-)")
                 (map #(Integer/parseInt %) $)
                 (partition 2 $))]
    {:field field
     :ranges values}))

(defn parse-input [input-str]
  (let [[rules-raw my-ticket-raw nearby-tickets-raw] (str/split input-str #"\n\n")
        my-ticket (map #(Integer/parseInt %) (rest (str/split my-ticket-raw #"[\n,]")))
        nearby-tickets (->>
                        nearby-tickets-raw
                        (str/split-lines)
                        (rest) ; remove header
                        (map parse-ticket))
        rules (->>
               rules-raw
               (str/split-lines)
               (map parse-rule))]
    [rules my-ticket nearby-tickets]))

(defn check-rule [rule field]
  (let [[[low-1 high-1] [low-2 high-2]] (rule :ranges)]
    (or
     (<= low-1 field high-1)
     (<= low-2 field high-2))))

(defn check-field [rules field]
  (some #(check-rule % field) rules))

(defn find-invalid-fields [rules ticket]
  (remove #(check-field rules %) ticket))

(defn solve-part-1 [rules my-ticket nearby-tickets]
  (reduce + (flatten (map #(find-invalid-fields rules %) nearby-tickets))))

(defn check-ticket [rules ticket]
  (every? #(check-field rules %) ticket))

(defn find-possible-fields-positions-one [rules ticket]
  "Return {fieldname #{possibility1 possibility2}"
  (into {} (for [rule rules]
            (let [fields-results (map #(check-rule rule %) ticket)
                  possible-positions (set (keep-indexed #(when %2 %1) fields-results))]
              [(rule :field) possible-positions]))))

(defn find-possible-fields-positions [rules tickets]
  (map #(find-possible-fields-positions-one rules %) tickets))

(defn determine-field-positions [fields-possible-positions]
  (loop [acc {} possible-positions fields-possible-positions]
    (if (every? empty? (vals possible-positions))
      acc
      (let [[current-field current-value-set] (->>
                (seq possible-positions)
                (filter #(= 1 (count (second %))))
                (first) ; input guarantees there is only one single choice field
                )
            current-value (first current-value-set)
            new-acc (assoc acc current-field current-value)
            new-possible-positions (into {} (for [[field possible-values] (seq possible-positions)] [field (disj possible-values current-value)]))]
        (recur new-acc new-possible-positions)))))

(defn intersection-possible-positions [possibility1 possibility2]
  (into {}
        (for [field (keys possibility1)]
          [field
           (set/intersection
            (possibility1 field)
            (possibility2 field))])))

(defn find-fields-positions [rules nearby-tickets]
  (let [valid-tickets (filter #(check-ticket rules %) nearby-tickets)
        possible-fields-positions (find-possible-fields-positions rules valid-tickets)
        fields-positions-set (reduce intersection-possible-positions possible-fields-positions)]
    (determine-field-positions fields-positions-set)))

(defn inspect-ticket [fields-positions ticket]
  (into {} (for [[field position] fields-positions]
             [field (nth ticket position)])))

(defn calculate-answer [ticket]
  (->>
   (seq ticket)
   (filter #(str/starts-with? (first %) "departure"))
   (map second)
   (reduce *)))

(defn solve-part-2 [rules my-ticket nearby-tickets]
  (let [fields-positions (find-fields-positions rules nearby-tickets)
        my-parsed-ticket (inspect-ticket fields-positions my-ticket)]
    (calculate-answer my-parsed-ticket)))

(defn -main
  [& args]
  (let [[rules my-ticket nearby-tickets] (parse-input (slurp "resources/input.txt"))]
    (println "part 1:" (solve-part-1 rules my-ticket nearby-tickets))
    (println "part 2:" (solve-part-2 rules my-ticket nearby-tickets))))
