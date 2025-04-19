package config

import (
	"os"

	"github.com/joho/godotenv"
)

type Config struct {
	OpenAIAPIKey    string
	CakeResumeAPIToken string
	GithubUsername  string
}

func LoadConfig() (Config, error) {
	err := godotenv.Load()
	if err != nil {
		return Config{}, err
	}

	cfg := Config{
		OpenAIAPIKey:    os.Getenv("OPENAI_API_KEY"),
		CakeResumeAPIToken: os.Getenv("CAKERESUME_API_TOKEN"),
		GithubUsername:  os.Getenv("GITHUB_USERNAME"),
	}

	return cfg, nil
}
