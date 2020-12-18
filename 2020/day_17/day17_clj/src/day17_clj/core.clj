(ns day17-clj.core
  (:require
   [clojure.string :as str]
   [clojure.set :as set])
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

(defn get-neighbors [[x y z]]
  (set
   (for [x' (range (- x 1) (inc (+ x 1)))
         y' (range (- y 1) (inc (+ y 1)))
         z' (range (- z 1) (inc (+ z 1)))
         :let [neighbor [x' y' z']]
         :when (not= neighbor [x y z])]
     neighbor)))

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

(defn -main
  [& args]
  (def world (parse-input (slurp "resources/input.txt")))
  (solve-part-1 world 6))
