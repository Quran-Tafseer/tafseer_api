package config

import "fmt"

type Service struct {
	Addr string `yaml:"addr" env:"ADDR" env-default:"localhost"`
	Port string `yaml:"port" env:"PORT" env-default:"8080"`
	Env  string `yaml:"env" env:"ENV" env-default:"dev"`
}

func (svc Service) FullAddress() string {
	return fmt.Sprintf("%s:%s", svc.Addr, svc.Port)
}
