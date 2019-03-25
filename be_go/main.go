package main

import (
	"crypto/rand"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"

	"github.com/gomarkdown/markdown"
)

//UserAuth - name/pass - used for login/signup
type UserAuth struct {
	Name string `json:"name"`
	Pass string `json:"pass"`
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
	http.HandleFunc("/signin", signIn)
	http.HandleFunc("/signup", signUp)
	http.HandleFunc("/", serveHelp)
	log.Fatal(http.ListenAndServe(":3344", nil))

}
