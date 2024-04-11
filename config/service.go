package config

import "fmt"

type Service struct {
	Addr string `fig:"addr" default:"localhost"`
	Port string `fig:"port" default:"1323"`
	Env  string `fig:"env" default:"dev"`
}

func (svc Service) FullAddress() string {
	return fmt.Sprintf("%s:%s", svc.Addr, svc.Port)
}
