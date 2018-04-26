int air, co;
int tmp;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
  tmp = analogRead(A0);
  air = map(tmp, 0, 1023, 0, 1000);
  tmp = analogRead(A1);
  co = map(tmp, 0, 1023, 0, 1000);
  Serial.println(String(air) + ", "+ String(co));
  delay(500);
}
