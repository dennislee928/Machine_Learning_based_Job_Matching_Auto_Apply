package main

import (
	"fmt"
	"log"
	"main/client"
	"main/config"
)

func main() {
	cfg, err := config.LoadConfig()
	if err != nil {
		log.Fatalf("Error loading config: %v", err)
	}

	fmt.Println("Golang fetcher service started")

	// Example usage:
	err = client.SubmitCakeResumeApplication(cfg.CakeResumeAPIToken, "12345")
	if err != nil {
		log.Printf("Error submitting to CakeResume: %v", err)
	}

	err = client.Submit104Application(cfg.GithubUsername, "67890")
	if err != nil {
		log.Printf("Error submitting to 104: %v", err)
	}
}