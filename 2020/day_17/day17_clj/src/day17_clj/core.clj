(ns day17-clj.core
  (:require
   [clojure.string :as str]
   [clojure.set :as set]
   [clojure.math.combinatorics :as combo])
  (:gen-class))

(defn parse-line [line]
  (->>
   line
   (map vector (range))
   (filter #(= \# (second %)))
   (map first)))

(defn product [[x ys]]
  (for [y ys] [x y]))

(defn parse-input [input-str]
  (->>
   input-str
   (str/split-lines)
   (map parse-line)
   (map vector (range))
   (map product)
   (apply concat) ; flatten one level to get all [x y]
   (map #(conj % 0))
   (set))) ; add z =0

(defn get-neighbors [coords]
  (let [ranges (map #(range (- % 1) (inc (+ % 1))) coords)
        neighbors-plus-current (apply combo/cartesian-product ranges)
        neighbors (disj (set neighbors-plus-current) coords)]
    neighbors))

(defn get-world-plus-neighbors [world]
  (reduce set/union world (map get-neighbors world)))

(defn new-state [world cube]
  (let [is-active (contains? world cube)
        count-active-neighbors (count (set/intersection world (get-neighbors cube)))]
    (if is-active
      (or (= 2 count-active-neighbors) (= 3 count-active-neighbors))
      (= 3 count-active-neighbors))))

(defn new-world [world]
  (let [cubes (get-world-plus-neighbors world)]
    (set (filter #(new-state world %) cubes))))

(defn solve-part-1 [world n]
  (count
   (nth
    (iterate new-world world)
    n)))

(defn solve-part-2 [world n]
  (let [hyper-world (set (map #(conj % 0) world))]
    (count
     (nth
      (iterate new-world hyper-world)
      n))))

(defn -main
  [& args]
  (def world (parse-input (slurp "resources/input.txt")))
  (println "part 1:" (solve-part-1 world 6))
  (time (println "part 2:" (solve-part-2 world 6))))
