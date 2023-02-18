go test -cover
go test -coverprofile=coverage.out
go tool cover -func=coverage.out
go tool cover -html=coverage.out
go test -cpuprofile=cpu.out
go tool pprof cpu.out
go test ./...
