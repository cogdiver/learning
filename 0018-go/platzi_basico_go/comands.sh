go get golang.org/x/website/tour
go get -v golang.org/x/website/tour
go get -v -u golang.org/x/website/tour
go get -v -u github.com/labstack/echo
go mod edit -replace=exampl e. com/greetings=…/greetings

go mod verify

go mod edit -dropreplace …
go mod vendor
go mod tidy