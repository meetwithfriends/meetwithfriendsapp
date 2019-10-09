package main

import (
	"crypto/rand"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"

	bolt "github.com/boltdb/bolt"
	"github.com/gomarkdown/markdown"
	"github.com/gorilla/mux"
)

//DBase type used for storing BoltDB instance
type DBase struct {
	DB       *bolt.DB
	Settings map[string]string
}

//Token used for tokens array.
type Token struct {
	Name  string `json:"name"`
	Token string `json:"token"`
}

//Err used for error handling in http requests
type Err struct {
	Code int    `json:"code"`
	Text string `json:"text"`
}

//UserAuth - name/pass - used for login/signup
type UserAuth struct {
	Name string `json:"name"`
	Pass string `json:"pass"`
}

var dB DBase
var auth DBase

var tokens map[string]string

// EnableCors Adds CORS to header
func EnableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
}

// CORSHandler getting everythign work for CORS
func CORSHandler(w http.ResponseWriter, req *http.Request) {
	setupResponse(&w, req)
}

// getting everythign work for CORS
func setupResponse(w *http.ResponseWriter, req *http.Request) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
	(*w).Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
	(*w).Header().Set("Access-Control-Allow-Headers", "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization")
}

// GenerateGUID generates UUID/GUID
func GenerateGUID() string {
	b := make([]byte, 16)
	rand.Read(b)
	return fmt.Sprintf("%X-%X-%X-%X-%X", b[0:4], b[4:6], b[6:8], b[8:10], b[10:])
}

func signUp(w http.ResponseWriter, r *http.Request) {
	var auth UserAuth
	print(auth.Name)
	print(auth.Pass)
}

func signIn(w http.ResponseWriter, r *http.Request) {

}

func serveHelp(w http.ResponseWriter, r *http.Request) {
	file, _ := ioutil.ReadFile("readme.md")
	output := markdown.ToHTML(file, nil, nil)
	w.Write(output)
}

func main() {
	tokens = make(map[string]string)
	auth = initAuthBase()
	router := mux.NewRouter()
	router.HandleFunc("/", serveHelp).Methods("GET")
	router.HandleFunc("/signin", signInEndpoint).Methods("POST")
	router.HandleFunc("/signin", CORSHandler).Methods("OPTIONS")
	log.Fatal(http.ListenAndServe(":3344", router))

}
