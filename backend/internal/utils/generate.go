package utils

import "github.com/bwmarrin/snowflake"

var (
	userGenerator *snowflake.Node
)

func init() {
	// Epoch is at 8/12/2022 18:50:00
	snowflake.Epoch = 1670521800000

	node, err := snowflake.NewNode(1)
	if err != nil {
		panic(err)
	}
	userGenerator = node
}

func GenerateUserId() string {
	return userGenerator.Generate().String()
}
