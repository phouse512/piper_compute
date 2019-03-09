package piper_compute

import (
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"strings"
)

func main() {
	// Initialize a session in us-west-2 that the SDK will use to load
	// credentials from the shared credentials file ~/.aws/credentials.
	sess, _ := session.NewSession(&aws.Config{
		Region: aws.String("us-west-2")},
	)

	// Create S3 service client
	svc := s3.New(sess)

	svc.PutObject((&s3.PutObjectInput{}).
		SetBucket("myBucket").
		SetKey("myKey").
		SetBody(strings.NewReader("object body")).
		SetWebsiteRedirectLocation("https://example.com/something"),
	)
}
