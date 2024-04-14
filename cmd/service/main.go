package main

import service "tafseer_api"

func main() {
	if err := service.Run(); err != nil {
		panic(err)
	}
}
